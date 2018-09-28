# Problems from : https://www.acmicpc.net/problem/14501
# Samsung SW 역량 테스트

# get input
N = int(input().split(' ')[0])
table = list()
for _ in range(N):
    table.append([int(x) for x in input().split(' ')])

maximum = 0
def calculate(day, wage):
    global table, N, maximum
    if N < day:
        raise IndexError
    elif N == day:
        return day, wage
    else:
        for i in range(day, N):
            d, w = day, wage
            try:
                d = i + table[i][0]
                w += table[i][1]
                d, w = calculate(d, w)
            except IndexError:
                d, w = day, wage
                continue
            if maximum < w:
                maximum = w
        return d, w

if __name__ == "__main__":
    calculate(0, 0)
    print(maximum)
