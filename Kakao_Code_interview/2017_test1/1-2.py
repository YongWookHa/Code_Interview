# http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
# 두번째 문제

def read_input():    
    with open("1-2/1-2_input.txt", "r") as f:
        inp = f.readlines()
        f.close()
       
    inp = [x.split()[0] for x in inp]
    
    return inp

def compute_score(input):
    point = re.compile('[0-9]+').findall(input)
    mul = re.compile('[\D]+').findall(input)
    special = []

    for i, m in enumerate(mul):
        if len(m) == 1:
            special.append(None)
        else:
            special.append(m[1])
            mul[i] = m[0]

    for i in range(3):
        point[i] = int(point[i])
        if mul[i] == 'S':
            pass
        elif mul[i] == 'D':
            point[i] = point[i] ** 2
        elif mul[i] == 'T':
            point[i] = point[i] ** 3

        if special[i] != None:
            
            if special[i] == '*':
                point[i] = point[i] * 2
                if i != 0:
                    point[i-1] = point[i-1] * 2
            elif special[i] == '#':
                point[i] = -1 * point[i]
                
    return sum(point)
                        
if __name__ == '__main__':
    inp = read_input()
    for input in inp:
        print(compute_score(input))
    
    
            
    
   
                
                    