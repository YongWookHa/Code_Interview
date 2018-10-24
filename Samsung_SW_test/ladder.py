# Problems from : https://www.acmicpc.net/problem/15684
# Samsung SW 역량 테스트

from itertools import permutations

# get inputs
N, M, H = map(int, input().split()[:3])
_nl = [0 for _ in range(N+1)]  # number of lines : include left of first line & right of last line
_map = [[0 for _ in range(N-1)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split()[:2])
    _map[a-1][b-1] = 1
    _nl[b] += 1

def solution(cnt, col=0):
    global N, H, _map
    result = 9999
    if check(_map):
        return cnt
    if cnt is 3:
        return result
    for n in range(col, N):
        for h in range(H):
            if N == 2:  # if there's only 1 line
                if _map[h][n-1] is 0:
                    _map[h][n - 1] = 1
                    result = min(solution(cnt+1, n), result)
                    _map[h][n - 1] = 0
            elif n is 1:  # first line
                if _map[h][n - 1] is 0 and _map[h][n] is 0:
                    _map[h][n - 1] = 1
                    result = min(solution(cnt+1, n), result)
                    _map[h][n - 1] = 0
            elif n is N-1:  # last line
                if _map[h][n-2] is 0 and _map[h][n-1] is 0:
                    _map[h][n - 1] = 1
                    result = min(solution(cnt+1, n), result)
                    _map[h][n - 1] = 0
            else:
                if _map[h][n-2] is 0 and _map[h][n-1] is 0 and _map[h][n] is 0:
                    _map[h][n-1] = 1
                    result = min(solution(cnt+1, n), result)
                    _map[h][n-1] = 0

    return result

def check(m):  # check if it's answer
    global N, H
    for n in range(N-1):
        look = n
        for h in range(H):
            if look is 0:
                r = m[h][look]
                if r:
                    look += 1
            elif look is N-1:
                l = m[h][look-1]
                if l:
                    look -= 1
            else:
                l, r = m[h][look-1], m[h][look]
                if l:
                    look -= 1
                elif r:
                    look += 1
        if n != look:
            return False
    return True

if __name__ == "__main__":
    ans = solution(0)
    if ans <= 3:
        print(ans)
    else:
        print(-1)



