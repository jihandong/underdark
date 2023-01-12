import math
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
            print("1d20 = 1, huge failure!")
        elif val == 20:
            print("1d20 = 20, huge success!")
        else:
            print("1d20 = %d" % val)
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
                print("%s = %d" % (expr, val))
            else:
                print("%s = %d = %s" % (expr, val, res))
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
    result = eval_add(expr)
    print(result)
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
# Common
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

#############################################################################
# init: load player data
#############################################################################

test1 = {
    "pl"    : True,
    "name"  : "jhd",

    "IN"    : 4,
    "HP"    : 8,
    "AC"    : 11,

    "str"   : -1,
    "dex"   : -1,
    "con"   : 0,
    "int"   : 2,
    "wis"   : -1,
    "cha"   : 0,

    "fort"  : 0,
    "ref"   : -1,
    "will"  : -1,

    "attack" : {
        "keyboard" : {
            "attack" : -1,
            "damage" : "1d4-1"
        },
        "mouse" : {
            "attack" : -1,
            "damage" : "1d4-1"
        }
    },

    "acrobatics"    : 1,
    "arcana"        : 1,
    "athletics"     : 1,
    "crafting"      : 1,
    "deception"     : 1,
    "diplomacy"     : 1,
    "intimidation"  : 1,
    "lore1"         : 1,
    "lore2"         : 1,
    "medicine"      : 1,
    "nature"        : 1,
    "occultism"     : 1,
    "performance"   : 1,
    "religion"      : 1,
    "society"       : 1,
    "stealth"       : 1,
    "survival"      : 1
}

test2 = {
    "pl"    : True,
    "name"  : "boss",

    "IN"    : 3,
    "HP"    : 7,
    "AC"    : 10,

    "str"   : -1,
    "dex"   : -2,
    "con"   : -1,
    "int"   : 3,
    "wis"   : 1,
    "cha"   : 2,

    "fort"  : 0,
    "ref"   : -1,
    "will"  : -1,

    "attack" : {
        "keyboard" : {
            "attack" : -1,
            "damage" : "1d4-1"
        },
        "mouse" : {
            "attack" : -1,
            "damage" : "1d4-1"
        }
    },

    "acrobatics"    : 1,
    "arcana"        : 1,
    "athletics"     : 1,
    "crafting"      : 1,
    "deception"     : 1,
    "diplomacy"     : 1,
    "intimidation"  : 1,
    "lore1"         : 1,
    "lore2"         : 1,
    "medicine"      : 1,
    "nature"        : 1,
    "occultism"     : 1,
    "performance"   : 1,
    "religion"      : 1,
    "society"       : 1,
    "stealth"       : 1,
    "survival"      : 1
}

characters = { "jhd" : test1, "boss" : test2 }

def cmd_init():
    return

#############################################################################
# Set
#############################################################################

def cmd_set(name, key, value):
    try:
        print("set %s's %s to %s" % (name, key, value))
        characters[name][key] = int(value)
    except:
        print("!!! Error Target: %s %s %s" % (name, key, value))
    return

#############################################################################
# Adjust
#############################################################################

def cmd_adjust(name, key, value):
    try:
        old_value = int(characters[name][key])
        new_value = old_value + int(value)
        print("adjust %s's %s from %d to %d" % (name, key, old_value, new_value))
        characters[name][key] = new_value
    except:
        print("!!! Error Target: %s %s %s" % (name, key, value))
    return

#############################################################################
# Check
#############################################################################

def cmd_check(name1, skill1, bonus1="", name2="", skill2="", bonus2=""):
    try:
        print("------------------------------")
        check1 = match_check(skill1)
        print("%s does %s check ..." % (name1, check1))
        result1 = cmd_roll("1d20+" + bonus1 + "+" + str(characters[name1][check1]))
        print("------------------------------")
        if (name2):
            check2 = ""
            if (skill2):
                check2 = check1
            else:
                check2 = match_check(skill2)
            print("... while %s does %s check ..." % (name2, check2))
            result2 = cmd_roll("1d20+" + bonus2 + "+" + str(characters[name2][check2]))
            if (result1 < result2):
                print("... and %s wins" % name2)
            elif (result1 > result2):
                print("... and %s wins" % name1)
            else:
                print("... and tie")
            print("------------------------------")
    except KeyError:
        print("!!! Error Target")
    return

#############################################################################
# Attack
#############################################################################

def cmd_attack(name1, name2, weapon, abonus="", dbonus="", acbonus=""):
    try:
        print("------------------------------")
        print("%s attack with %s%d ..." % (name1, weapon,\
              characters[name1]["attack"][weapon]["attack"]))
        attack = cmd_roll("1d20+" + abonus + "+" +\
                          str(characters[name1]["attack"][weapon]["attack"]))
        print("------------------------------")
        ac = cmd_roll(str(characters[name1]["AC"]) + acbonus)
        print("... and %s has AC=%d ..." % (name2, ac))
        print("------------------------------")
        if (attack >= ac):
            print("... cause damage")
            damage = cmd_roll(characters[name1]["attack"][weapon]["damage"]\
                     + "+" + dbonus)
        else:
            print("... miss")
        print("------------------------------")
    except KeyError:
        print("!!! Error Target: %s %s %s" % (name1, name2, weapon))

    return

#############################################################################
# Dump
#############################################################################

def cmd_dump(name=""):
    print("---------+----------+----------+-------------------+-----------------------")
    print("    name | IN HP AC | ft rf wl | st dx cn it ws ch | weapon")
    print("---------+----------+----------+-------------------+-----------------------")
    for c in characters.values():
        try:
            weapons = ""
            for w in c["attack"].keys():
                weapons += w
                weapons += " "
            print("%8s | %2d %2d %2d | %2d %2d %2d | %2d %2d %2d %2d %2d %2d | %s"
                  % (c["name"], c["IN"], c["HP"], c["AC"],
                     c["fort"], c["ref"], c["will"],
                     c["str"], c["dex"], c["con"],
                     c["int"], c["wis"], c["cha"], weapons))
        except KeyError:
            print("!!! Error Json")
    print("---------+----------+----------+-------------------+-----------------------")
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
        #print("prepare  : add a monster")
        #print("start    : roll initiative")
        #print("stop     : clear monsters")
        print("set      : change some values")
        print("           set name key value")
        print("adjust   : adjust some values")
        print("           adjust name key value")
        print("check    : roll ability/save/skill check")
        print("           check name skill [bonus] [enemy] [skill] [bonus]")
        print("           check name skill")
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
        elif (argv[0] == "set"):
            if (len(argv) >= 4):
                cmd_set(argv[1], argv[2], argv[3])
            else:
                print("!!! Error Args")
        elif (argv[0] == "adjust"):
            if (len(argv) >= 4):
                cmd_adjust(argv[1], argv[2], argv[3])
            else:
                print("!!! Error Args")
        elif (argv[0] == "check"):
            if (len(argv) >= 7):
                # check player skill [bonus] [monster] [skill] [bonus]
                cmd_check(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6])
            elif (len(argv) >= 6):
                cmd_check(argv[1], argv[2], argv[3], argv[4], argv[5])
            elif (len(argv) >= 5):
                cmd_check(argv[1], argv[2], argv[3], argv[4])
            elif (len(argv) >= 4):
                cmd_check(argv[1], argv[2], argv[3])
            elif (len(argv) >= 3):
                cmd_check(argv[1], argv[2])
            else:
                print("!!! Error Args")
        elif (argv[0] == "attack"):
            if (len(argv) >= 7):
                # attack player monster weapon [atk_bonus] [dmg_bonus] [ac_bonus]
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
                cmd_dump(argv[1])
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
