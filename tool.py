import copy
import json
import math
import os
import random
import re

#############################################################################
# Roll Dices
#############################################################################

def eval_roll(expr):
    # advantage for dnd5e
    if expr == "g" or expr == "good" or expr == "advantage" or expr == "adv":
        val1 = random.randint(1, 20)
        val2 = random.randint(1, 20)
        val  = max(val1, val2)
        if val == 1:
            print("advantage = 1 = max(1, 1), huge failure")
        elif val == 20:
            print("advantage = 20 = max(%d, %d), huge success!" % (val1, val2))
        else:
            print("advantage = %d = max(%d, %d)" % (val, val1, val2))
        return val

    #  disadvantage for dnd5e
    if expr == "b" or expr == "bad" or expr == "disadvantage" or expr == "disad":
        val1 = random.randint(1, 20)
        val2 = random.randint(1, 20)
        val  = min(val1, val2)
        if val == 1:
            print("disadvantage = 1 = min(%d, %d), huge failure" % (val1, val2))
        elif val == 20:
            print("disadvantage = 20 = min(20, 20), huge success!")
        else:
            print("disadvantage = %d = min(%d, %d)" % (val, val1, val2))
        return val

    # elf feat
    if expr == "e" or expr == "elf":
        val1 = random.randint(1, 20)
        val2 = random.randint(1, 20)
        val3 = random.randint(1, 20)
        val  = max(val1, val2, val3)

    # standard d20
    if expr == "d" or expr == "D":
        val = random.randint(1, 20)
        if val == 1:
            print("| 1d20 = \033[31m1 !\033[0m")
        elif val == 20:
            print("| 1d20 = \033[32m20 !\033[0m")
        else:
            print("| 1d20 = %d" % val)
        return val

    # mDx
    result = re.match('([0-9]+)[Dd]([0-9]+)', expr)
    if result:
        if (result.group(1).isdigit() and result.group(2).isdigit()):
            nb = int(result.group(1))
            if nb == 0:
                print("!!! Error Number: ", expr)
                return 0

            dice = int(result.group(2))
            if dice == 0:
                print("!!! Error Dice: ", expr)
                return 0

            val = 0
            res = ""
            for i in range(0, nb):
                roll = random.randint(1, dice)
                val = val + roll
                if i == 0:
                    res = str(roll)
                else:
                    res = res + " + " + str(roll)

            if nb == 1:
                print("| %s = %d" % (expr, val))
            else:
                print("| %s = %d = %s" % (expr, val, res))
            return val
        else:
            print("!!! Error Expression: ", expr)
            return 0

    # Dx
    result = re.match('[Dd]([0-9]+)', expr)
    if result:
        if (result.group(1).isdigit()):
            dice = int(result.group(1))
            if dice == 0:
                print("!!! Error Dice: ", expr)
                return 0

            roll = random.randint(1, dice)
            print("%s = %d" % (expr, roll))
            return roll
        else:
            print("!!! Error Expression: ", expr)
            return 0


    # const integer
    result = re.match('[0-9]+', expr)
    if result:
        if (expr.isdigit()):
            return int(expr)

    return 0;

def eval_minus(expr):
    result = re.split('[\s]*\-[\s]*', expr)
    result = map(eval_roll, result)
    result = map(lambda x : -x, result)
    result = list(result)
    result[0] = -result[0]
    result = sum(result)
    return result

def eval_add(expr):
    result = re.split('[\s]*\+[\s]*', expr)
    result = map(eval_minus, result)
    result = sum(result)
    return result

def cmd_roll(expr):
    print("+----------------------")
    result = eval_add(expr)
    print("| %d = %s" % (result, expr))
    return result

#############################################################################
# make character
#############################################################################

def cmd_character(expr):
    result = [[0 for i in range(4)] for i in range(6)]
    for i in range(0, 6):
        for j in range(0, 4):
            result[i][j] = random.randint(1, 6)
    result = list(map(lambda x : sum(x) - min(x), result))
    result.sort()
    print(result)
    return

#############################################################################
# Common Data
#############################################################################

checks = [
    "str",
    "dex",
    "con",
    "int",
    "wis",
    "cha",
    "fort",
    "ref" ,
    "will",
    "acrobatics"  ,
    "arcana"      ,
    "athletics"   ,
    "crafting"    ,
    "deception"   ,
    "diplomacy"   ,
    "intimidation",
    "lore1"       ,
    "lore2"       ,
    "medicine"    ,
    "nature"      ,
    "occultism"   ,
    "performance" ,
    "religion"    ,
    "society"     ,
    "stealth"     ,
    "survival"
]

def match_check(name):
    for c in checks:
        if name in c:
            return c
    return "wtf"

character_path = "/home/jhd/Downloads/underdark/character"
monster_path   = "/home/jhd/Downloads/underdark/monster"
active_objects = {}

# init: load character profiles
def cmd_init():
    for root, dirs, files in os.walk(character_path):
        for filename in files:
            try:
                path = os.path.join(root, filename)
                f = open(path)
                content = f.read()
                object = json.loads(content)
                object["initiative"] = 0
                active_objects[object["name"]] = object
            except KeyError:
                print("!!! Error Json: %s" % filename)
    cmd_dump()
    return

# prepare: load a monster profile
def cmd_prepare(name, num=1):
    for root, dirs, files in os.walk(monster_path):
        for filename in files:
            try:
                if (name in filename):
                    path = os.path.join(root, filename)
                    f = open(path)
                    content = f.read()
                    object = json.loads(content)
                    if (object["name"] in active_objects.keys()):
                        print("!!! Error Existed: %s" % filename)
                    else:
                        num = int(num)
                        if (num > 1):
                            while (num > 0):
                                num = num - 1
                                obj = copy.deepcopy(object)
                                obj["initiative"] = 0
                                obj["name"] = obj["name"] + str(num)
                                active_objects[obj["name"]] = obj
                        else:
                            object["initiative"] = 0
                            active_objects[object["name"]] = object
            except:
                print("!!! Error Json: %s" % filename)
    cmd_dump()
    return

# start: roll initiative for active objects and sort
def cmd_start():
    for obj in active_objects.values():
        try:
            obj["initiative"] = cmd_roll("1d20+" + str(obj["IN"]));
        except KeyError:
            print("!!! Error Key")
    cmd_dump()
    return

# stop: remove all monsters
def cmd_stop():
    names = list(active_objects.keys())
    for key in names:
        try:
            active_objects[key]['initiative'] = 0
            if (not active_objects[key]["pl"]):
                active_objects.pop(key)
        except KeyError:
            print("!!! Error Key")
    cmd_dump()
    return

#############################################################################
# Set
#############################################################################

def cmd_set(name, key, value):
    try:
        print("set %s's %s to %s" % (name, key, value))
        active_objects[name][key] = int(value)
    except:
        print("!!! Error Target: %s %s %s" % (name, key, value))
    return

#############################################################################
# Adjust
#############################################################################

def cmd_add(name, key, value):
    try:
        old_value = int(active_objects[name][key])
        new_value = old_value + int(value)
        print("adjust %s's %s from %d to %d" % (name, key, old_value, new_value))
        active_objects[name][key] = new_value
    except:
        print("!!! Error Target: %s %s %s" % (name, key, value))
    return

#############################################################################
# Check
#############################################################################

def cmd_check(name, skill, bonus=""):
    try:
        skill = match_check(skill)
        print("%s check %s ..." % (name, skill))
        result = cmd_roll("D+" + bonus + "+" + str(active_objects[name][skill]))
    except KeyError:
        print("!!! Error Target")
    return

#############################################################################
# Attack
#############################################################################

def cmd_attack(name1, name2, weapon, abonus="", dbonus="", acbonus=""):
    try:
        print("+----------------------")
        print("| ATK: %s use %s%d" % (name1, weapon,\
              active_objects[name1]["attack"][weapon]["attack"]))
        attack = cmd_roll("D+" + abonus + "+" +\
                          str(active_objects[name1]["attack"][weapon]["attack"]))
        ac = active_objects[name1]["AC"]
        if (acbonus):
            print("+----------------------")
            print("| AC: %s has %s bonus" % (name2, acbonus))
            ac = cmd_roll(str(ac) + "+" + acbonus)
        print("+----------------------")
        if (attack >= ac):
            if (dbonus):
                print("| HIT: %s has %s bonus" % (name1, dbonus))
            else:
                print("| HIT")
            damage = cmd_roll(active_objects[name1]["attack"][weapon]["damage"]\
                     + "+" + dbonus)
            cmd_dump([name2])
        else:
            print("| \033[33mMISS\033[0m")
    except KeyError:
        print("!!! Error Target: %s %s %s" % (name1, name2, weapon))

    return

# dump: show active objects
def cmd_dump(names=[]):
    print("+--+----------+----------+----------+-------------------+-----------------------")
    print("|  |     name | IN HP AC | ft rf wl | st dx cn it ws ch | weapon")
    print("+--+----------+----------+----------+-------------------+-----------------------")
    sorted_objects = sorted(active_objects.values(), key=lambda x : -x["initiative"])
    for c in sorted_objects:
        try:
            weapons = ""
            for w in c["attack"].keys():
                weapons += w
                weapons += " "
            if (c["name"] in names):
                if (c["pl"]):
                    print("|%2d| \033[34m%8s\033[0m | %2d %2d %2d | %2d %2d %2d | %2d %2d %2d %2d %2d %2d | %s"
                            % (c["initiative"], c["name"] , c["IN"], c["HP"], c["AC"],
                            c["fort"], c["ref"], c["will"],
                            c["str"], c["dex"], c["con"],
                            c["int"], c["wis"], c["cha"], weapons))
                else:
                    print("|%2d| \033[34m%-8s\033[0m | %2d %2d %2d | %2d %2d %2d | %2d %2d %2d %2d %2d %2d | %s"
                            % (c["initiative"], c["name"] , c["IN"], c["HP"], c["AC"],
                            c["fort"], c["ref"], c["will"],
                            c["str"], c["dex"], c["con"],
                            c["int"], c["wis"], c["cha"], weapons))
            else:
                if (c["pl"]):
                    print("|%2d| %8s | %2d %2d %2d | %2d %2d %2d | %2d %2d %2d %2d %2d %2d | %s"
                            % (c["initiative"], c["name"], c["IN"], c["HP"], c["AC"],
                            c["fort"], c["ref"], c["will"],
                            c["str"], c["dex"], c["con"],
                            c["int"], c["wis"], c["cha"], weapons))
                else:
                    print("|%2d| %-8s | %2d %2d %2d | %2d %2d %2d | %2d %2d %2d %2d %2d %2d | %s"
                            % (c["initiative"], c["name"], c["IN"], c["HP"], c["AC"],
                            c["fort"], c["ref"], c["will"],
                            c["str"], c["dex"], c["con"],
                            c["int"], c["wis"], c["cha"], weapons))
        except KeyError:
            print("!!! Error Json")
    print("+--+----------+----------+----------+-------------------+-----------------------")
    return

#############################################################################
# Dist
#############################################################################

def cmd_dist(a, b):
    try:
        x = int(a)
        y = int(b)
        print("distance %d, %d is %f" % (x, y, math.sqrt(x * x + y * y)))
    except:
        print("!!! Error A B")
    return


#############################################################################
# process_command
#############################################################################

def process_command(expr):
    if (expr == ""):
        return
    elif (expr == "q" or expr == "quit"):
        exit()
    elif (expr == "h" or expr == "help"):
        #print("init     : init characters")
        print("prepare  : add a monster")
        print("start    : roll initiative")
        print("stop     : remove monsters")
        print("set      : change some values")
        print("           set name key value")
        print("add      : add adjust values")
        print("           add name key value")
        print("check    : roll ability/save/skill check")
        print("           check name skill [bonus]")
        print("attack   : rool attack and damage")
        print("           attack name target weapon [attack] [damage] [bonus]")
        print("           attack name target weapon")
        return
    else:
        argv = re.split('[\s]+', expr)
        if (argv[0] == "char"):
            cmd_character(argv[1])
        elif (argv[0] == "init"):
            cmd_init()
        elif (argv[0] == "prepare"):
            if (len(argv) >= 3):
                cmd_prepare(argv[1], argv[2])
            elif (len(argv) >= 2):
                cmd_prepare(argv[1])
            else:
                print("!!! Error Args")
        elif (argv[0] == "start"):
            cmd_start()
        elif (argv[0] == "stop"):
            cmd_stop()
        elif (argv[0] == "set"):
            if (len(argv) >= 4):
                cmd_set(argv[1], argv[2], argv[3])
            else:
                print("!!! Error Args")
        elif (argv[0] == "add"):
            if (len(argv) >= 4):
                cmd_add(argv[1], argv[2], argv[3])
            else:
                print("!!! Error Args")
        elif (argv[0] == "check"): # check player skill [bonus]
            if (len(argv) >= 4):
                cmd_check(argv[1], argv[2], argv[3])
            elif (len(argv) >= 3):
                cmd_check(argv[1], argv[2])
            else:
                print("!!! Error Args")
        elif (argv[0] == "attack"): # attack player monster weapon [atk_bonus] [dmg_bonus] [ac_bonus]
            if (len(argv) >= 7):
                cmd_attack(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6])
            elif (len(argv) >= 6):
                cmd_attack(argv[1], argv[2], argv[3], argv[4], argv[5])
            elif (len(argv) >= 5):
                cmd_attack(argv[1], argv[2], argv[3], argv[4])
            elif (len(argv) >= 4):
                cmd_attack(argv[1], argv[2], argv[3])
            else:
                print("!!! Error Args")
        elif (argv[0] == "dump"):
            if (len(argv) >= 2):
                cmd_dump(argv[1:])
            else:
                cmd_dump()
        elif (argv[0] == "dist"):
            if (len(argv) >= 3):
                cmd_dist(argv[1], argv[2])
            else:
                print("!!! Error Args")
        else:
            cmd_roll(expr)

    print("")
    return

#############################################################################
# mainloop
#############################################################################

cmd_init()
while True:
    expr = input("trpg> ")
    expr = re.split('[\s]*\#', expr)
    process_command(expr[0])
