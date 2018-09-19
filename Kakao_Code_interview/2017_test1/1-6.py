# http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
# 여섯번째 문제

def read_input(): 
    with open('1-6/1-6_input.txt', 'r') as f:
        lines = f.readlines()
    m, n, board = [], [], []
    for x in lines:
        line = x.split()
        m.append(int(line[0]))
        n.append(int(line[1]))
        board.append(line[2].split(','))
    return m, n, board
        
def friends_block(m, n, board):
    # restruct the block with shape (n x b)
    b = [[board[j][i]for j in reversed(range(m))] for i in range(n)] 
    deleted_block = 0
    while(True):
        match = False
        match_map = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n-1):
            for j in range(m-1):
                if b[i][j] != 'X' and b[i][j] == b[i][j+1] == b[i+1][j] == b[i+1][j+1]:
                    match_map[i][j], match_map[i][j+1], match_map[i+1][j], match_map[i+1][j+1] = (True, True, True, True)
                    match = True
        for row in match_map:
            deleted_block += row.count(True) 

        if not match:
            break
        else:
            for i in range(n):
                for j in reversed(range(m)): # delete upper block first
                    if match_map[i][j]:
                        del b[i][j]
                        b[i].append('X')
            
    return deleted_block

if __name__ == '__main__':
    _m, _n, _board = read_input()
    results = list(map(friends_block, _m, _n, _board))
    for result in results:
        print(result)
