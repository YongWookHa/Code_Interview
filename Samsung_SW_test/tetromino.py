# Problems from : https://www.acmicpc.net/problem/14500
# Samsung SW 역량 테스트

###############get input###################
inp = input().split(' ')[:2]
N, M = int(inp[0]), int(inp[1])
_map = list()
for _ in range(N):
    t = input().split(' ')[:M]
    _map.append([int(x) for x in t])
############################################

def play_game(_map, N, M):

    # index #
    # 1 2 3 4
    # 5 6 7
    # 8 9
    # 10

    def calculate(n, m):
        nonlocal _map
        result = dict()
        iter = 1
        for i in range(4):
            for j in range(4-i):
                result[iter] = _map[n+i][m+j]
                iter += 1
        return result

    # all the cases (19)
    candidate = [[1,2,3,4],[1,5,8,10],[1,2,5,6],[1,5,8,9],[2,6,8,9],[1,2,3,5],[1,2,3,7],[1,2,5,8],[1,2,6,9],
                 [1,5,6,7],[3,5,6,7],[1,5,6,9],[2,5,6,8],[2,3,5,6],[1,2,6,7],[2,5,6,7],[1,5,6,8],[2,5,6,9],[1,2,3,6]]
    maximum = 0

    # padding
    for _ in range(3):
        _map.append([0 for _ in range(M)])
    for i, row in enumerate(_map):
        _map[i] = row + [0 for _ in range(3)]

    # solving
    for n in range(N):
        for m in range(M):
            try:
                cal = calculate(n, m)
            except IndexError as e:
                continue

            for cand in candidate:
                res = 0
                for c in cand:
                    if cal[c] < 0:
                    res += cal[c]
                    if maximum <= res:
                        maximum = res
    return maximum

if __name__ == "__main__":
    print(play_game(_map, N, M))
