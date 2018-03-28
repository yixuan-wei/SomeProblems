'''
定义字符串运算；字符串仅限于A-Za-z0-9的所有组合；
按照优先级排列：
（）括号
～将字符串顺序颠倒；-改变字符串大小写
* 如 AAA*BB = ABBABBA；/ 如ABCABCAE/AB = CCE
+ 将两个字符串串一起；- 前者减后者（完全），如ABCDEF-DE = ABCF
'''
import sys
for line in sys.stdin:
    a = line.split()
    form = a[0]
    res = []


    def isstring(each):
        if 'z' >= each >= 'a' or '0' <= each <= '9' or 'A' <= each <= 'Z':
            return True
        else:
            return False


    for each in form:
        if isstring(each):
            if len(res) > 0 and isinstance(res[-1], str) and isstring(res[-1]):
                res[-1] += each
            else:
                res.append(each)
        elif each == '+':
            res.append(-1)
        elif each == '-':
            res.append(1)
        elif each == '*':
            res.append(-2)
        elif each == '/':
            res.append(2)
        elif each == '~':
            res.append(3)
        elif each == '(':
            res.append(4)
        elif each == ')':
            res.append(0)
    for k in range(len(res)):
        if res[k] == 1:
            if k == 0 or not isstring(res[k - 1]):
                res[k] = -3


    def findmax(res):
        maxi = 0
        pos = 0
        for m in range(len(res)):
            if isinstance(res[m], int) and abs(res[m]) > maxi:
                pos = m
                maxi = res[m]
        return pos


    def findP(res):
        maxi = 0
        for p in range(len(res)):
            if res[p] == 0:
                maxi = p
        return maxi


    def calculate(res):
        if len(res) == 0:
            return ""
        if len(res) == 1:
            return res[0]
        pp = findmax(res)
        if res[pp] == 4:
            end = findP(res[pp:]) + pp
            return calculate(res[:pp] + [calculate(res[pp + 1:end])] + res[end + 1:])
        elif abs(res[pp]) == 3:
            if isstring(res[pp + 1]):
                if res[pp] == 3:
                    res[pp + 1] = res[pp + 1][::-1]
                else:
                    for c in range(len(res[pp + 1])):
                        if 'A' <= res[pp + 1][c] <= 'Z':
                            res[pp + 1][c].lower()
                        elif 'a' <= res[pp + 1][c] <= 'z':
                            res[pp + 1][c].upper()
                res.pop(pp)
                return calculate(res)
            else:
                for c in range(len(res[pp + 2])):
                    if 'A' <= res[pp + 2][c] <= 'Z':
                        res[pp + 2][c].lower()
                    elif 'a' <= res[pp + 2][c] <= 'z':
                        res[pp + 2][c].upper()
                res[pp + 1] = res[pp + 1][::-1]
                res.pop(pp)
                res.pop(pp)
                return calculate(res)

        elif res[pp] == 2:
            t = ""
            for ea in res[pp - 1]:
                if ea not in res[pp + 1]:
                    t += ea
            res[pp] = t
            res.pop(pp - 1)
            res.pop(pp)
            return calculate(res)
        elif res[pp] == -2:
            t = ""
            for ea in res[pp - 1][:-1]:
                t += ea + res[pp + 1]
            res[pp - 1] = t + res[pp - 1][-1]
            res.pop(pp)
            res.pop(pp)
            return calculate(res)
        elif res[pp] == 1:
            l = len(res[pp + 1])
            t = ""
            q = 0
            while q <= len(res[pp - 1]) - l:
                if res[pp - 1][q:q + l] == res[pp + 1]:
                    q += l
                    t += res[pp - 1][q:]
                    break
                else:
                    t += res[pp - 1][q]
                    q += 1
            res[pp - 1] = t
            res.pop(pp)
            res.pop(pp)
            return calculate(res)
        elif res[pp] == -1:
            res[pp - 1] += res[pp + 1]
            res.pop(pp)
            res.pop(pp)
            return calculate(res)


    print(calculate(res))
