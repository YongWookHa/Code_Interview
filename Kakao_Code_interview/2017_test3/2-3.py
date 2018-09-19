# http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
# 세번째문제

import re

def read_inputs():
    with open("2-3/2-3_inputs.txt","r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line[-1:] is '\n':
            line = line[:-1]
        lines[i] = line.split(', ')
    return lines

def file_sort(inputs):
    def spliter(s):
        head = re.compile('[a-zA-Z]+').findall(s)[0]
        number = re.compile('[0-9]+').findall(s)[0]
        return (head.lower(), int(number))
    result = sorted(inputs, key=spliter)
    return result
    
if __name__ == "__main__":
    inputs = read_inputs()
    results = list(map(file_sort, inputs))
    for result in results:
        print(result)
        