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
# init: load player data
#############################################################################

test1 = {
    "pl"    : True,
    "name"  : "jhd",

    "IN"    : 4,
    "HP"    : 8,
    "AC"    : 11,

    "str"   : 8,
    "dex"   : 9,
    "con"   : 10,
    "int"   : 14,
    "wis"   : 8,
    "cha"   : 10,

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

    "acrobatics"    : 3,
    "arcana"        : 4
}

test2 = {
    "pl"    : True,
    "name"  : "boss",

    "IN"    : 4,
    "HP"    : 8,
    "AC"    : 11,

    "str"   : 8,
    "dex"   : 9,
    "con"   : 10,
    "int"   : 14,
    "wis"   : 8,
    "cha"   : 10,

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

    "acrobatics"    : 3,
    "arcana"        : 4
}

characters = [ test1, test2 ]

def cmd_init():
    return

#############################################################################
# Attack
#############################################################################

def cmd_attack(name, weapon, abonus = "", dbonus = ""):
    for c in characters:
        if c["name"] == name:
            try:
                print("Roll attack check for %s with %s" % (name, weapon))
                result1 = cmd_roll("1d20+" + abonus) + c["attack"][weapon]["attack"]
                print("Roll damage check for %s with %s" % (name, weapon))
                result2 = cmd_roll(c["attack"][weapon]["damage"] + "+" + dbonus)
            except:
                print("!!! Error Character: %s %s" % (name. value))
            break
    return

#############################################################################
# Dump
#############################################################################

def cmd_dump(name=""):
    print("---------+----------+---------------+-------------------------")
    print("    mame | IN HP AC | fort ref will | str dex con int wis cha")
    print("---------+----------+---------------+-------------------------")
    for c in characters:
        try:
            print("%8s | %2d %2d %2d | %4d %3d %4d | %3d %3d %3d %3d %3d %3d"
                  % (c["name"], c["IN"], c["HP"], c["AC"],
                     c["fort"], c["ref"], c["will"],
                     c["str"], c["dex"], c["con"],
                     c["int"], c["wis"], c["cha"]))
        except KeyError:
            print("!!! Error")
    print("---------+----------+---------------+-------------------------")
    return

#############################################################################
# process_command
#############################################################################

commands = {
    "char"    : cmd_character,
    "init"    : cmd_init,
    #"prepare" : cmd_prepare,
    #"start"   : cmd_start,
    #"stop"    : cmd_stop,
    #"set"     : cmd_set,
    #"add"     : cmd_add,
    #"check"   : cmd_check,
    #"attack"  : cmd_attack,
    "dump"    : cmd_dump,
    "roll"    : cmd_roll,
}

def process_command(expr):
    if (expr == ""):
        return
    elif (expr == "q" or expr == "quit"):
        exit()
    else:
        argv = re.split('[\s]+', expr)
        if (argv[0] == "char"):
            cmd_character(argv[1])
        elif (argv[0] == "init"):
            cmd_init()
        elif (argv[0] == "attack"):
            if (len(argv) >= 5):
                cmd_attack(argv[1], argv[2], argv[3], argv[4])
            elif (len(argv) >= 4):
                cmd_attack(argv[1], argv[2], argv[3])
            else:
                cmd_attack(argv[1], argv[2])
        elif (argv[0] == "dump"):
            if (len(argv) >= 2):
                cmd_dump(argv[1])
            else:
                cmd_dump()

    return

#############################################################################
# mainloop
#############################################################################

while True:
    expr = input("trpg> ")
    expr = re.split('[\s]*\#', expr)
    process_command(expr[0])

