# Problems from : https://www.acmicpc.net/problem/14499
# Samsung SW 역량 테스트

from copy import copy

###############get input###################
inp = input().split(' ')[:5]
N, M, _x, _y, K = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]), int(inp[4])
_map = list()
_order = list()  # 주사위 이동 명령
for _ in range(N):
    inp = input().split(' ')[:M]
    _map.append([int(x) for x in inp])

inp = input().split(' ')[:K]
_order = [int(x) for x in inp]  # 1:동 2:서 3:북 4:남
############################################

class rolling_dice():
    def __init__(self, original_map, start_position):
        self._map = [copy(x) for x in original_map]  # deep copy
        self.p = start_position  # position
        start = self.get_val(self.p[0], self.p[1])
        self.set_val(0, self.p[0], self.p[1])
        self.dice = [[0, 0, 0, start], [0, 0, 0, start]]  # [[서 윗 동 밑], [북 윗 남 밑]]

    def get_val(self, x, y):
        if x < 0 or y < 0:
            raise IndexError
        return self._map[x][y]

    def set_val(self, val, x, y):
        self._map[x][y] = val

    def roll_dice(self, direc):
        x = self.p[0]
        y = self.p[1]
        if direc == 1:  # 동쪽
            y += 1
            temp = list()
            try:
                bottom = self.get_val(x, y)
            except IndexError as e:
                return
            if bottom == 0:
                self.set_val(self.dice[0][2], x, y) # map 갱신
                temp += [self.dice[0][3], self.dice[0][0], self.dice[0][1], self.dice[0][2]]
            else:
                self.set_val(0, x, y)
                temp += [self.dice[0][3], self.dice[0][0], self.dice[0][1], bottom]
            self.dice[0] = temp
            self.dice[1][1], self.dice[1][3] = self.dice[0][1], self.dice[0][3]  # sync 윗, 밑

        if direc == 2:  # 서쪽
            y -= 1
            temp = list()
            try:
                bottom = self.get_val(x, y)
            except IndexError as e:
                return
            if bottom == 0:
                self.set_val(self.dice[0][0], x, y)
                temp += [self.dice[0][1], self.dice[0][2], self.dice[0][3], self.dice[0][0]]
            else:
                self.set_val(0, x, y)
                temp += [self.dice[0][1], self.dice[0][2], self.dice[0][3], bottom]
            self.dice[0] = temp
            self.dice[1][1], self.dice[1][3] = self.dice[0][1], self.dice[0][3]  # sync 윗, 밑

        if direc == 3:  # 북쪽
            x -= 1
            temp = list()
            try:
                bottom = self.get_val(x, y)
            except IndexError as e:
                return
            if bottom == 0:
                self.set_val(self.dice[1][0], x, y)
                temp += [self.dice[1][1], self.dice[1][2], self.dice[1][3], self.dice[1][0]]
            else:
                self.set_val(0, x, y)
                temp += [self.dice[1][1], self.dice[1][2], self.dice[1][3], bottom]
            self.dice[1] = temp
            self.dice[0][1], self.dice[0][3] = self.dice[1][1], self.dice[1][3]  # sync 윗, 밑

        if direc == 4:  # 남쪽
            x += 1
            temp = list()
            try:
                bottom = self.get_val(x, y)
            except IndexError as e:
                return
            if bottom == 0:
                self.set_val(self.dice[1][2], x, y)
                temp += [self.dice[1][3], self.dice[1][0], self.dice[1][1], self.dice[1][2]]
            else:
                self.set_val(0, x, y)
                temp += [self.dice[1][3], self.dice[1][0], self.dice[1][1], bottom]
            self.dice[1] = temp
            self.dice[0][1], self.dice[0][3] = self.dice[1][1], self.dice[1][3]  # sync 윗, 밑

        self.p[0], self.p[1] = x, y
        print(self.dice[0][1])


def play_game(original_map, start_position, order):
    game = rolling_dice(original_map, start_position)
    for o in order:
        game.roll_dice(o)
    return 0


if __name__ == "__main__":
    play_game(_map, [_x, _y], _order)
