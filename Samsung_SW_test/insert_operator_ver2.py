# Problems from : https://www.acmicpc.net/problem/14888
# Samsung SW 역량 테스트

# get inputs
N = int(input().split()[0])
A = [int(x) for x in input().split()]
a, b, c, d = map(int, input().split())
maximum, minimum = -1000000000, 1000000000

# accelerated solution
def solution(a,b,c,d, idx, crnt_res):  # DFS, without copying arr
    global A, maximum, minimum

    if a+b+c+d == 0:
        maximum = max(maximum, crnt_res)
        minimum = min(minimum, crnt_res)

    if a:
        solution(a-1, b, c, d, idx+1, crnt_res+A[idx+1])  # recursive
    if b:
        solution(a, b-1, c, d, idx+1, crnt_res-A[idx+1])
    if c:
        solution(a, b, c-1, d, idx+1, crnt_res*A[idx+1])
    if d:
        solution(a, b , c, d-1, idx+1, int(crnt_res/A[idx+1]))

if __name__ == "__main__":
    solution(a, b, c, d, 0, A[0])
    print(maximum)
    print(minimum)
