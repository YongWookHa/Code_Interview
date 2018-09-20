from copy import deepcopy

###########get input##############
N = int(input())
_map = list()
for i in range(N):
    line = input().split(' ')
    _map.append([int(x) for x in line])

MAX = sum([sum(x) for x in _map])
maximum = max(max(x) for x in _map)
directions = ['right', 'left', 'up', 'down', ]


def bumpAndSum(li):
    s = list()
    result = list()
    for x in li:
        if x != 0:
            if not s:
                s.append(x)
                continue
            if len(s) == 1:
                if x == s[0]:
                    s.append(x)
                    result.append(sum(s))
                    s = list()
                else:
                    result.append(s[0])
                    s = [x]
    if s:
        result.append(s[0])
    result = result + [0] * (len(li) - len(result))  # 0 붙여줌
    return result


def tilt_board(ori_map, direc):
    crnt_map = deepcopy(ori_map)
    if direc == 'up':
        temp = [[crnt_map[i][j] for i in range(N)] for j in range(N)] # transpose
        for i, t in enumerate(temp):
            crnt_map[i] = bumpAndSum(t)
        crnt_map = [[crnt_map[i][j] for i in range(N)] for j in range(N)]
    if direc == 'down':
        temp = [[crnt_map[i][j] for i in range(N)] for j in range(N)]
        for i, t in enumerate(temp):
            li = bumpAndSum(list(reversed(t)))
            crnt_map[i] = list(reversed(li))
        crnt_map = [[crnt_map[i][j] for i in range(N)] for j in range(N)]
    if direc == 'left':
        for i, t in enumerate(ori_map):
            crnt_map[i] = bumpAndSum(t)
    if direc == 'right':
        for i, t in enumerate(ori_map):
            li = bumpAndSum(list(reversed(t)))
            crnt_map[i] = list(reversed(li))

    return crnt_map


def play_game(ori_map, num=1):
    global N, _map, MAX, maximum, directions
    if num > 5:
        return

    for d in directions:
        crnt_map = deepcopy(ori_map)
        crnt_map = tilt_board(crnt_map, d)
        if crnt_map == ori_map:
            continue
        temp = max(max(crnt_map, key=lambda a: max(a)))
        if temp == MAX:
            maximum = MAX
            return
        if maximum < temp:
            maximum = temp
        play_game(crnt_map, num + 1)


if __name__ == "__main__":
    play_game(_map)
    print(maximum)