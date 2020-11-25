from itertools import permutations

def operate(a, b, op) -> float:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return a / 0.0001
        else:
            return a / b

def solve(nums: tuple, target: int = 24) -> None:
    op = ("+", "-", "*", "/")
    answer = []
    opAns = []
    j = 1
    res = nums[0]
    temp1 = temp2 = 0
    found = planB = planC = planD = False
    allAns = []
    p = (*{*permutations(nums)},)
    ansappend = allAns.append
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
                        found = True
                        answer = [*numPer]
                        opAns = [a, b, c]
                        tempList = [answer, opAns]
                        ansappend(tempList)
                    if c == "/" and b != "/":
                        j -= 1
                        res = temp2
                    elif c == "/" and b == "/":
                        j = 1
                        res = numPer[0]
                    else:
                        res = temp1

    if found:
        print("\n".join("{0} {4} {1} {5} {2} {6} {3}".format(*answer, *opAns) for answer, opAns in allAns))

    allAns *= 0

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
                        answer = [*numPer]
                        opAns = [a, c, b]
                        tempList = [answer, opAns]
                        ansappend(tempList)

    if found and planB:
        print("\n".join("({0} {4} {1}) {5} ({2} {6} {3})".format(*answer, *opAns) for answer, opAns in allAns))

    allAns *= 0

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
                        answer = [numPer[3], numPer[2], numPer[0], numPer[1]]
                        opAns = [c, b, a]
                        tempList = [answer, opAns]
                        ansappend(tempList)

    if found and planC:
        print("\n".join("{0} {4} ({1} {5} ({2} {6} {3}))".format(*answer, *opAns) for answer, opAns in allAns))

    allAns *= 0

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
                        ansappend(tempList)

    if found and planD:
        print("\n".join("{0} {4} (({1} {5} {2}) {6} {3})".format(*answer, *opAns) for answer, opAns in allAns))

    if not found:
        print("Solution not found !")


def main() -> None:
    print("<----- Math 24Solver ----->")
    nums: Tuple[int] = ()
    while -1 not in nums or len(nums) != 1:
        print("Enter four numbers separated by space, : (Enter -1 to quit)")
        try:
            nums = (*(int(i) for i in input().strip().split()),)
        except ValueError:
            pass
        if len(nums) == 4:
            solve(nums, 24)
            nums *= 0


if __name__ == "__main__":
    main()
