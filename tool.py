import random
import re

def eval_roll(expr):
    # 优势
    if expr == "g" or expr == "good" or expr == "advantage" or expr == "adv":
        val1 = random.randint(1, 20)
        val2 = random.randint(1, 20)
        val  = max(val1, val2)
        if val == 1:
            print("优势 = 1 = max(1, 1), 属实是没救了")
        elif val == 20:
            print("优势 = 20 = max(%d, %d), 大成功!" % (val1, val2))
        else:        
            print("优势 = %d = max(%d, %d)" % (val, val1, val2))
        return val

    # 劣势
    if expr == "b" or expr == "bad" or expr == "disadvantage" or expr == "disad":
        val1 = random.randint(1, 20)
        val2 = random.randint(1, 20)
        val  = min(val1, val2)
        if val == 1:
            print("劣势 = 1 = min(%d, %d), 大失败" % (val1, val2))
        elif val == 20:
            print("劣势 = 20 = min(20, 20), 真的离谱!")
        else:
            print("劣势 = %d = min(%d, %d)" % (val, val1, val2))
        return val

    # 精灵之准
    if expr == "e" or expr == "elf":
        val1 = random.randint(1, 20)
        val2 = random.randint(1, 20)
        val3 = random.randint(1, 20)
        val  = max(val1, val2, val3)

    # 标准d20
    if expr == "d" or expr == "D":
        val = random.randint(1, 20)
        if val == 1:
            print("1d20 = 1, 大失败!")
        elif val == 20:
            print("1d20 = 20, 大成功!")
        else:
            print("1d20 = %d" % val)
        return val

    # 若干同种骰子
    result = re.match('([0-9]+)[Dd]([0-9]+)', expr)
    if result:
        nb = int(result.group(1))
        if nb == 0:
            print("错误的骰子数: ", expr)
            return 0

        dice = int(result.group(2))
        if dice == 0:
            print("错误的骰子: ", expr)
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

    # 一个骰子
    result = re.match('[Dd]([0-9]+)', expr)
    if result:
        dice = int(result.group(1))
        if dice == 0:
            print("错误的骰子: ", expr)
            return 0

        roll = random.randint(1, dice)
        print("%s = %d" % (expr, roll))
        return roll

    # 常数
    result = re.match('[0-9]+', expr)
    if result:
        return int(expr)

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
    
def eval(expr):
    if (len(expr) == 0):
        return

    if (expr == "char" or expr == "character"):
        result = [[0 for i in range(4)] for i in range(6)]
        for i in range(0, 6):
            for j in range(0, 4):
                result[i][j] = random.randint(1, 6)
        print(result)
        result = list(map(lambda x : sum(x) - min(x), result))
        result.sort()
        print("4d6去掉最低值，得到六个属性值为", result, "\n")
        return

    print("检定结果 = %d\n" % eval_add(expr))

while True:
    expr = input("==> ")
    expr = re.split('[\s]*\#', expr)
    eval(expr[0])
