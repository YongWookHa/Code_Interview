# Problems from : https://www.acmicpc.net/problem/14502
# Samsung SW 역량 테스트


def get_input():
    N = [int(n) for n in input().split(' ')[:2]]
    _map = list()
    for i in range(N[0]):
        _map.append([int(x) for x in input().split(' ')[:N[1]]])
    return N[0], N[1], _map


def spreadAndCount(_map):
    def count_safe(_map):
        count = (len(_map))*(len(_map[0]))
        for row in _map:
            count = count - row.count(1) - row.count(2)
        return count

    result = [x[:] for x in _map]
    N = len(_map)
    M = len(_map[0])
    while(True):
        temp = [x[:] for x in result]
        for i in range(1, N-1):
            for j in range(1, M-1):
                if result[i][j] is 2:
                    if result[i-1][j] is not 1:
                        result[i - 1][j] = 2
                    if result[i+1][j] is not 1:
                        result[i + 1][j] = 2
                    if result[i][j-1] is not 1:
                        result[i][j-1] = 2
                    if result[i][j+1] is not 1:
                        result[i][j+1] = 2
        if temp == result:
            return count_safe(result)


def set_wall(_map, num=1):
    def check_8neighbor(inp_map, n, m):  # 8 neighbor
        score = 0
        for a in range(n - 1, n + 2):
            for b in range(m - 1, m + 2):
                if inp_map[a][b] == 1:
                    score += 1
        if score >= 1:
            return True
        else:
            return False

    N = len(_map)
    M = len(_map[0])
    crnt_map = [x[:] for x in _map]  # deep copy

    maximum = 0
    count = 0
    # set candidate
    candidate = list()
    for n in range(1, N-1):
        for m in range(1, M-1):
            if crnt_map[n][m] == 0 and check_8neighbor(crnt_map, n, m):
                candidate.append((n, m))

    for w in candidate:
        crnt_map[w[0]][w[1]] = 1  # set wall
        if num == 1:
            count = set_wall(crnt_map, num + 1)
            crnt_map[w[0]][w[1]] = 3  # 지나갔던 곳
        if num == 2:
            count = set_wall(crnt_map, num + 1)
            crnt_map[w[0]][w[1]] = 4  # 지나갔던 곳
        if num == 3:
            count = spreadAndCount(crnt_map)  # spread the plague And measure the area of safe zone
            crnt_map[w[0]][w[1]] = 5  # 지나갔던 곳
            if maximum < count:
                maximum = count
            continue

        if maximum < count:
            maximum = count

    return maximum


def isolate(_map):
    M = len(_map[0])
    # padding
    inp_map = [[1 for _ in range(M)]] + _map
    for i, m in enumerate(inp_map):
        inp_map[i] = [1] + m + [1];
    inp_map.append([1 for _ in range(M+2)])

    res = set_wall(inp_map)  # dynamic programming, DFS

    return res


if __name__ == "__main__":
    N, M, _map = get_input()
    result = isolate(_map)
    print(result)
