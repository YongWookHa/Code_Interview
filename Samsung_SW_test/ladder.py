# Problems from : https://www.acmicpc.net/problem/15684
# Samsung SW 역량 테스트

from itertools import permutations

# get inputs
N, M, H = map(int, input().split()[:3])
_nl = [0 for _ in range(N+1)]  # number of lines : include left of first line & right of last line
_map = [[0 for _ in range(N+1)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split()[:2])
    _map[a-1][b] = 1
    _nl[b] += 1

def prove_map(cnt, col=1): # DFS
    global N, H, _map
    result = 9999
    if check(_map):
        return cnt
    if cnt is 3:
        return result
    for n in range(N-col, 0, -1):
        for h in range(H):
            if _map[h][n-1] is 0 and _map[h][n] is 0 and _map[h][n+1] is 0:
                _map[h][n] = 1
                result = min(prove_map(cnt+1, N-n), result)
                _map[h][n] = 0

    return result

def check(m):  # check if it's answer
    global N, H
    for n in range(1, N+1):
        look = n
        for h in range(H):
            l, r = m[h][look-1], m[h][look]
            if l:
                look -= 1
            elif r:
                look += 1
        if n != look:
            return False
    return True


if __name__ == "__main__":
    ans = prove_map(0)
    if ans <= 3:
        print(ans)
    else:
        print(-1)



