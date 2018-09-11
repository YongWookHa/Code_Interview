# http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
# 네번째 문제

import re

FIRST_BUS = 9 * 60 

def read_input():    
    with open("1-4/1-4_input.txt", "r") as f:
        inp = f.readlines()
        f.close()
    inp = [line.split() for line in inp]

    n = [int(x[0]) for x in inp]
    t = [int(x[1]) for x in inp]
    m = [int(x[2]) for x in inp]
    time_table = [x[3:] for x in inp]

    return n, t, m, time_table
                        
    
def shuttle_bus(n, t, m, time_table):
    def time_to_int(time):
        H = int(time[0:2])
        M = int(time[3:5])
        return 60 * H + M
    
    def int_to_time(i):
        return '%s:%s' % (str(i//60).zfill(2), str(i%60).zfill(2))
    
    timeTable = sorted(list(map(time_to_int, time_table)))
    pair_table = list(timeTable)
    tup = [m, -1] # [available seats, index of left crew]
    bt = FIRST_BUS # bus time
    for bt in range(FIRST_BUS, FIRST_BUS+(n-1)*t+1, t):
        tup[0] = m
        for _ in range(len(timeTable)):
            crew = timeTable[0]
            if crew <= bt and 1 < tup[0]:
                del timeTable[0]
                tup[0] -= 1
                tup[1] += 1
            elif crew <= bt and tup[0] is 1:
                del timeTable[0]
                tup[0] -= 1
                tup[1] += 1
                break
    
    if tup[0] == 0: # available seats of last bus 
        return int_to_time( pair_table[tup[1]]-1 )
    else:
        return int_to_time(FIRST_BUS+(n-1)*t)
    
if __name__ == '__main__':
    n, t, m, time_table = read_input()
    results = list(map(shuttle_bus, n, t, m, time_table))
    for result in results:
        print(result)

                
                    