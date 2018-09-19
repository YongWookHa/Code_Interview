# http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
# 세번째 문제

import re

def read_input():    
    with open("1-3/1-3_input.txt", "r") as f:
        inp = f.readlines()
        f.close()
       
    cacheSize = [int(x[0]) for x in inp]
    inputs = [re.compile('[a-zA-Z]+').findall(x[1:]) for x in inp]
    inputs = [[y.lower() for y in x] for x in inputs]

    return cacheSize, inputs
                        
def cache_cost(cacheSize, cities):
    cache = dict()
    cost = 0
    
    for i, city in enumerate(cities):
        if city not in cache:
            if cacheSize == 0:
                cost += 5
                continue
            if len(cache) < cacheSize:
                cache[city] = i
            else:
                # print(list(cache.values()))
                least_used_index = list(cache.values()).index(min(cache.values()))
                least_used = list(cache.keys())[least_used_index]
                del cache[least_used]
                cache[city] = i
            cost += 5
        else:
            cache[city] = i
            cost += 1
            
    return cost

    
if __name__ == '__main__':
    cacheSize, inputs = read_input()
    costs = list(map(cache_cost, cacheSize, inputs))
    for cost in costs:
        print(cost)
                
                    