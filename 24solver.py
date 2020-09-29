from itertools import permutations

def operate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return a / 0.0001
        else:
            return a / b

def solve(nums, target):
    op = ('+', '-', '*', '/')
    answer = []
    opAns = []
    i = 1
    j = 1
    res = nums[0]
    temp1 = 0
    temp2 = 0
    found = False
    planB = False
    planC = False
    planD = False
    allAns = []
    p = list(set(permutations(nums)))

    for numPer in p:
        res = numPer[0]
        for a in op:
            # temp4 = res
            res = operate(res, numPer[j], a)
            # temp3 = numPer[j]
            temp2 = res
            j += 1
            for b in op:
                res = operate(res, numPer[j], b)
                temp1 = res
                j += 1
                for c in op:
                    res = operate(res, numPer[j], c)
                    if round(res, 3) == target:
                        """ print (target)
                        print (numPer)
                        print(temp4)
                        print (temp3)

                        print (temp2)
                        print (temp1)
                        print (a)
                        print (b)
                        print (c) """
                        found = True
                        answer = list(numPer)
                        opAns = [a, b, c]
                        tempList = [answer, opAns]
                        allAns.extend([tempList])
                    if c == '/' and b != '/':
                        j -= 1
                        res = temp2
                    elif c == '/' and b == '/':
                        j = 1
                        res = numPer[0]
                    else:
                        res = temp1

    if found:
        for temp in allAns:
            answer = temp[0]
            opAns = temp[1]
            ans = ''
            j = 0
            for i in range(4):
                ans += str(answer[i])
                if j < 3:
                    ans += ' '
                    ans += opAns[j]
                    ans += ' '
                j += 1
            print (ans)

    allAns.clear()

    for numPer in p:
        temp1 = 0
        temp2 = 0
        for a in op:
            temp1 = operate(numPer[0], numPer[1], a)
            for b in op:
                temp2 = operate(numPer[2], numPer[3], b)
                for c in op:
                    res = operate(temp1, temp2, c)
                    if round(res, 3) == target:
                        found = True
                        planB = True
                        """ print (numPer[0])
                        print (a)
                        print (numPer[1])
                        print (temp1)
                        print(c)
                        print (numPer[2])
                        print (b)
                        print (numPer[3])
                        print (temp2) """
                        answer = list(numPer)
                        opAns = [a, c, b]
                        tempList = [answer, opAns]
                        allAns.extend([tempList])

    if found and planB:
        for temp in allAns:
            answer = temp[0]
            opAns = temp[1]
            j = 0
            ans = '('
            for i in range(4):
                if i == 2:
                    ans += '('
                ans += str(answer[i])
                if i == 1 or i == 3:
                    ans += ')'
                if j < 3:
                    ans += ' '
                    ans += opAns[j]
                    ans += ' '
                j += 1
            print (ans)

    allAns.clear()

    j = 1
    for numPer in p:
        temp1 = 0
        temp2 = 0
        for a in op:
            temp1 = operate(numPer[0], numPer[1], a)
            for b in op:
                temp2 = operate(numPer[2], temp1, b)
                for c in op:
                    res = operate(numPer[3], temp2, c)
                    if round(res, 3) == target:
                        found = True
                        planC = True
                        """ print (numPer[3])
                        print (c)
                        print (numPer[2])
                        print (b)
                        print (numPer[0])
                        print (a)
                        print (numPer[1]) """
                        answer = [numPer[3], numPer[2], numPer[0], numPer[1]]
                        opAns = [c, b, a]
                        tempList = [answer, opAns]
                        allAns.extend([tempList])

    if found and planC:
        for temp in allAns:
            answer = temp[0]
            opAns = temp[1]
            j = 0
            ans = ''
            for i in range(4):
                if i == 1 or i == 2:
                    ans += '('
                ans += str(answer[i])
                if i == 3:
                    ans += ')'
                if j < 3:
                    ans += ' '
                    ans += opAns[j]
                    ans += ' '
                j += 1
            ans += ')'
            print(ans)

    allAns.clear()

    j = 1
    for numPer in p:
        temp1 = 0
        temp2 = 0
        for a in op:
            temp1 = operate(numPer[0], numPer[1], a)
            for b in op:
                temp2 = operate(temp1, numPer[2], b)
                for c in op:
                    res = operate(numPer[3], temp2, c)
                    if round(res, 3) == target:
                        found = True
                        planD = True
                        answer = [numPer[3], numPer[0], numPer[1], numPer[2]]
                        opAns = [c, a, b]
                        tempList = [answer, opAns]
                        allAns.extend([tempList])

    if found and planD:
        for temp in allAns:
            answer = temp[0]
            opAns = temp[1]
            j = 0
            ans = ''
            for i in range(4):
                if i == 1:
                    ans += '(('
                ans += str(answer[i])
                if i == 2 or i == 3:
                    ans += ')'
                if j < 3:
                    ans += ' '
                    ans += opAns[j]
                    ans += ' '
                j += 1
            print(ans)

    if not found:
        print ('Solution not found !')

if __name__ == "__main__":
    print ('<----- Math 24Solver ----->')
    nums = []
    while -1 not in nums or len(nums) != 1:
        print ('Enter four numbers separated by space, : (Enter -1 to quit)')
        try:
            nums = [int(i) for i in input().strip().split()]
        except ValueError:
            pass
        if len(nums) == 4 :
            solve(nums, 24)
            nums.clear()