# http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
# 다섯번째 문제

import re

def read_input():    
    with open("1-5/1-5_input.txt", "r") as f:
        inp = f.readlines()
        f.close()
        
    inp = [line.strip('\n') for line in inp]
    inp = [re.compile('[^,]+').findall(line) for line in inp]
    
    str1 = [line[0] for line in inp]
    str2 = [line[1] for line in inp]
    
    return str1, str2
                        
    
def news_clustering(str1, str2):
    
    def make_set(s):
        result = []
        eng = re.compile('[a-zA-Z]')
        for i in range(len(s)-1):
            match = eng.match(s[i])
            match_next = eng.match(s[i+1])
            if match and match_next:
                result.append(s[i]+s[i+1])
        return result
    
    
    d_set1 = make_set(str1.lower())
    d_set2 = make_set(str2.lower())
    
    set1, set2 = set(d_set1), set(d_set2)
    uni, inter = set1.union(set2), set1.intersection(set2)
    uni_counter, inter_counter = 0, 0
    
    if len(uni) == 0:
        return 65536
    
    for s in uni:
        if d_set1.count(s) > 1:
            uni_counter += max(d_set1.count(s), d_set2.count(s))
        else:
            uni_counter += 1
                            
    for s in inter:
        if d_set1.count(s) > 1:
            inter_counter += min(d_set1.count(s), d_set2.count(s))
        else:
            inter_counter += 1
            
    return int((inter_counter / uni_counter) * 65536)

if __name__ == '__main__':
    str1, str2 = read_input()
    results = list(map(news_clustering, str1, str2))
    for result in results:
        print(result)

                
                    