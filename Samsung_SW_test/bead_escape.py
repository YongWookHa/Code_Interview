# Problems from : https://www.acmicpc.net/problem/13460
# Samsung SW 역량 테스트

from copy import copy

################## get input ##################
inp = input()
inp = inp.split(' ')
row, col = int(inp[0]), int(inp[1])

m = list()
red_ball = [0, 0]  # point where red ball is
blue_ball = [0, 0]  # point where red ball is

for r in range(row):
    x = input()
    if 'R' in x:
        red_ball = [r, x.find('R')]
    if 'B' in x:
        blue_ball = [r, x.find('B')]
    m.append(list(x))
###############################################

possibilities = ['up', 'down', 'right', 'left']
oppo_direc = {'up': 'down', 'down': 'up', 'right': 'left', 'left': 'right'}
minimum = 11

def deepcopy(li):
    return [copy(x) for x in li]

def radar(crnt_map, direc, ball):
    x = ball[0]
    y = ball[1]
    if direc == 'up':
        return [crnt_map[x - i][y] for i in range(1, x)]
    if direc == 'down':
        return [crnt_map[x + i][y] for i in range(1, row - x - 1)]
    if direc == 'left':
        return [crnt_map[x][y - i] for i in range(1, y)]
    if direc == 'right':
        return [crnt_map[x][y + i] for i in range(1, col - y - 1)]


def move_ball(_map, direc, ball, ball_name):
    crnt_map = _map
    x = ball[0]
    y = ball[1]
    if x * y == 0:
        return crnt_map, ball
    if direc == 'up':
        crnt_map[x][y] = '.'
        crnt_map[x - 1][y] = ball_name
        ball = [x - 1, y]
    elif direc == 'down':
        crnt_map[x][y] = '.'
        crnt_map[x + 1][y] = ball_name
        ball = [x + 1, y]
    elif direc == 'left':
        crnt_map[x][y] = '.'
        crnt_map[x][y - 1] = ball_name
        ball = [x, y - 1]
    elif direc == 'right':
        crnt_map[x][y] = '.'
        crnt_map[x][y + 1] = ball_name
        ball = [x, y + 1]
    elif direc == 'O':  # when the ball goes to 'O'.
        crnt_map[x][y] = '.'
        ball = [0, 0]
    return crnt_map, ball


def tilt_board(_map, direc, r, b, _result=False):
    red_O, blue_O, result = False, False, _result
    crnt_map, red, blue = deepcopy(_map), r, b
    path_red = radar(crnt_map, direc, r)
    for x in path_red:
        if x is '.':
            crnt_map, red = move_ball(crnt_map, direc, red, 'R')
        elif x is 'O':
            crnt_map, red = move_ball(crnt_map, 'O', red, 'R')
            red_O = True
        else:  # when the ball meets '#' or 'B'.
            break
    path_blue = radar(crnt_map, direc, b)
    for x in path_blue:
        if x is '.':
            crnt_map, blue = move_ball(crnt_map, direc, blue, 'B')
        elif x is 'O':
            crnt_map, blue = move_ball(crnt_map, 'O', blue, 'B')
            blue_O = True
        else:  # when the ball meets '#' or 'R'.
            break

    if red_O is True and blue_O is False:
        result = True

    if _map != crnt_map:
        return tilt_board(crnt_map, direc, red, blue, result)
    else:
        return crnt_map, red, blue, result


def play_game(_map, red, blue, num=1, prev_direc=None):
    global minimum, oppo_direc, possibilities
    original_map = deepcopy(_map)
    if num > 10:
        # print('')
        return
        # print(prev_direc, red, blue, ' | ', end='')
    direc = deepcopy(possibilities)
    if prev_direc:
        try:
            direc.remove(oppo_direc[prev_direc])
            direc.remove(prev_direc)
        except ValueError as e:
            pass

    if not direc:
        return

    for d in direc:
        crnt_map, r, b, result = deepcopy(original_map), deepcopy(red), deepcopy(blue), False
        crnt_map, r, b, result = tilt_board(_map, d, r, b)
        if crnt_map == original_map or b == [0, 0]:
            continue
        if result:
            if num < minimum:
                minimum = num
            return
        else:
            play_game(crnt_map, r, b, num + 1, prev_direc=d)


if __name__ == "__main__":
    play_game(m, red_ball, blue_ball)
    if minimum > 10:
        print('-1')
    else:
        print(minimum)
