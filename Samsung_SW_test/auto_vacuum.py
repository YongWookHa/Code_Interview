# Problems from : https://www.acmicpc.net/problem/14501
# Samsung SW 역량 테스트

# get input
N, M = map(int, input().split()[:2])
r, c, d = map(int, input().split()[:3])
_map = list()
pre_score = 0
for _ in range(N):
    inp_row = [int(x) for x in input().split()[:M]]
    _map.append(inp_row)
    pre_score += inp_row.count(0)

def is_clean(a, b):
    global _map
    chk_list = [_map[a+1][b], _map[a-1][b], _map[a][b+1], _map[a][b-1]]
    for x in chk_list:
        if x == 0:
            return 0
    return 1

def score():
    global _map
    result = 0
    for row in _map:
        result += row.count(0)
    return result

def auto_vacuum():
    global _map, N, M, r, c, d
    is_back = False
    while True:
        d = d % 4
        if is_clean(r, c):
            is_back = True

        _map[r][c] = 2
        nr, nc = r, c
        if d == 0:  # north
            if is_back:
                r += 1
            else:
                nc -= 1
        elif d == 1:  # east
            if is_back:
                c -= 1
            else:
                nr -= 1
        elif d == 2:  # south
            if is_back:
                r -= 1
            else:
                nc += 1
        elif d == 3:  # west
            if is_back:
                c += 1
            else:
                nr += 1

        if is_back:
            is_back = False
            if _map[r][c] == 1:
                break
            continue

        if _map[nr][nc] == 0:
            r, c = nr, nc
        d -= 1
        # while ends
    return

if __name__ == "__main__":
    auto_vacuum()
    print(pre_score - score())
