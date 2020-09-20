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
            return a + b
        else:
            return a / b

def solve(nums, target):
    op = ['+', '-', '*', '/']
    answer = []
    opAns = []
    """ if (sum(nums) == target):
        for i in nums:
            answer += str(i)
            answer += plus
        answer.pop() """
    i = 1
    j = 1
    k = 0
    res = nums[0]
    temp1 = 0
    temp2 = 0
    found = False
    planB = False
    allAns = []
    p = permutations(nums)

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
                    if res == target:
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
                        opAns = []
                        opAns += a + b + c
                        tempList = [answer, opAns]
                        allAns.append(tempList)
                    if c == '/' and b != '/':
                        j -= 1
                        res = temp2
                    elif c == '/' and b == '/':
                        j = 1

                        res = numPer[0]
                    else:
                        res = temp1
                    """ if j >= 4:
                        if int(res) == 24:
                            found = True
                        res = nums[0]
                        j = 1 """

    if found and not planB:
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

    p = permutations(nums)
    for numPer in p:
        temp1 = 0
        temp2 = 0
        for a in op:
            temp1 = operate(numPer[0], numPer[1], a)
            for b in op:
                temp2 = operate(numPer[2], numPer[3], b)
                for c in op:
                    res = operate(temp1, temp2, c)
                    if res == target:
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
                        opAns = []
                        opAns += a + c + b
                        tempList = [answer, opAns]
                        allAns.append(tempList)

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

    if not found:
        print ('Solution not found !')



if __name__ == "__main__":
    print ('<----- Math 24Solver -----')
    nums = [0, 0]
    while nums[0] != -1 and len(nums) > 1:
        print ('Enter four numbers: (Enter -1 to quit)')
        nums = [int(i) for i in input().split()]
        if len(nums) == 4 :solve(nums, 24)