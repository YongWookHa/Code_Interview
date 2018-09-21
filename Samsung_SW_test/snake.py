# Problems from : https://www.acmicpc.net/problem/3190
# Samsung SW 역량 테스트

N = int(input()) # 보드 크기
K = int(input())
apple = list()
for _ in range(K):
    ap = input().split(" ")
    apple.append([int(ap[0]), int(ap[1])])
    
L = int(input())
move_list = dict()
for _ in range(L):
    mv = input().split(" ")
    X = int(mv[0])
    C = mv[1]
    move_list[X] = C

directions = ['up', 'right', 'down', 'left']
    
class snake():
    def __init__(self, loc):
        # head of snake => body[-1]
        self.body = [loc]
    def move(self, loc):
        del self.body[0]
        self.body.append(loc)
    def grow(self, loc):
        self.body.append(loc)
    def body(self):
        return self.body
    
def play_game():
    DI = 1 # direction index
    crnt_loc = [1,1]
    bam = snake(loc=crnt_loc)
    t = 0
    while(True):
        if DI % 2 == 0:
            crnt_loc[1] += 1 if DI % 4 == 0 else -1
        else:
            crnt_loc[0] += 1 if DI % 4 == 1 else -1
        t+=1 
        if N <= crnt_loc[0] or crnt_loc < 0:
            break
        if N <= crnt_loc[0] or crnt_loc < 0:
            break
        
        if crnt_loc in apple:
            apple.remove(crnt_loc) # eat apple
            bam.grow() # Increase the length
        else:
            if crnt_loc in bam.body():
                break
            else:
                bam.move(crnt_loc)
        if t in move_list.keys():
            d = move_list[t]
            if c == 'D': # right -> direction index + 1
                DI+=1 
            elif c == 'L': # left -> direction index - 1
                DI-=1 
    print(t)
         
if __name__ == "__main__":
    play_game()
            
            
            
        
        
        
        