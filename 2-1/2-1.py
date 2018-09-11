# http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
# 첫번째문제
import time

def read_inputs():
    with open("2-1/2-1_inputs.txt", "r") as f:
        lines = f.read().splitlines()
    for i, line in enumerate(lines):
        lines[i] = line.split(', ')
        for j, x in enumerate(lines[i]):
            lines[i][j] = int(x)
    return(lines)
    
def N_game(inputs):
    def convert(a, n): # 숫자 a를 n진법으로
        l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        result = []
        while(True):
            x, d = divmod(a, n)
            a = a // n
            result.append(l[d])
            if x == 0:
                break
        result.reverse()
        return result
    
    n, t, m, p = (inputs[0], inputs[1], inputs[2], inputs[3])
    num = 0 # number to convert
    turn = 1 # current turn
    result = []
    while(len(result) < t):
        cn = convert(num, n) # list of converted number
        for i in cn:
            if turn == p and len(result) < t:
                result.append(i)
            turn = turn+1 if turn % m is not 0 else 1
        num+=1
    return ''.join(str(x) for x in result)

if __name__ == "__main__":
    start_time = time.time()
    inp = read_inputs()
    results = list(map(N_game, inp))
    for result in results:
        print(result)
    print('spent time : ', time.time()-start_time)