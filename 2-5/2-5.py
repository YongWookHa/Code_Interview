# http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
# 다섯번째문제

import re

def read_input():
    with open("2-5/2-5_inputs.txt", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = re.findall('"(.+?)"', line)
    return lines

def auto_complete(inputs):
    table = dict()
    for w in inputs:
        for i in range(1, len(w)+1):
            if w[:i] not in table.keys():
                table[w[:i]] = w
                break
            elif table[w[:i]] is None:
                continue
            else: #  w[:i] in table.keys() && table[w[:i]] is not None
                prw = table[w[:i]] # previously registered word
                table[prw[:i]] = None # prw[:i] cannot represent a word
                table[prw[:i+1]] = prw
                
    result = 0
    for key in table.keys():
        if table[key] is not None:
            result += len(key)
            
    print(table)
    return result
    
if __name__ == "__main__":
    inputs = read_input()
    results = list(map(auto_complete, inputs))
    for result in results:
        print(result)
    