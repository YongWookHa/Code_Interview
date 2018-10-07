# Problems from : https://www.acmicpc.net/problem/14888
# Samsung SW 역량 테스트

# get inputs
N = int(input().split()[0])
A = [int(x) for x in input().split()]
oper = [int(x) for x in input().split()]
oper_dict = {'+': oper[0], '-': oper[1], '*': oper[2], '/': oper[3]}
operator = []
for key in oper_dict.keys():
    for j in range(oper_dict[key]):
        operator.append(key)

combi = []


def calculate(operator):  # operator list를 받아서 계산 진행
    global A
    operand = A[0]
    for i, op in enumerate(operator, 1):
        if op == '+':
            operand = operand + A[i]
        elif op == '-':
            operand = operand - A[i]
        elif op == '*':
            operand = operand * A[i]
        elif op == '/':
            operand = int(operand / A[i])
    return operand


def make_combination(oper_dict, arr=[]):  # 가능한 operator 조합을 만듦 - DFS
    global combi
    if sum(oper_dict.values()) == 0:  # 남은 후보가 없으면 하나의 후보 완성
        combi.append(arr)
        return
    else:
        for key in oper_dict.keys():
            if oper_dict[key] != 0:
                this_dict = oper_dict.copy()
                this_arr = arr[:]
                this_arr.append(key)
                this_dict[key] -= 1
                make_combination(this_dict, this_arr)
            else:
                pass


if __name__ == "__main__":
    maximum, minimum = -1000000000, 1000000000
    make_combination(oper_dict)
    # print(combi)
    # print('combi len:', len(combi))  # len(combi)는 nCr combination의 값.
    for c in combi:
        res = calculate(c)
        if res < minimum:
            minimum = res
        if res > maximum:
            maximum = res
    print(maximum)
    print(minimum)

