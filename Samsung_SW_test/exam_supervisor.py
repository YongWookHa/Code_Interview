# Problems from : https://www.acmicpc.net/problem/13458
# Samsung SW 역량 테스트

N = int(input())
R = input().split(' ')[:N]
room = [int(x) for x in R]
superviser = input().split(' ')[:2]
_B, _C = int(superviser[0]), int(superviser[1])

def caculate():
    result = 0
    for r in room:
        x = r - _B
        d, n = divmod(x, _C) 
        result += 1 # 총감독관
        if n:  
            result += d + 1
        else:
            result += d 
    return result

if __name__ == "__main__":
    print(caculate())
