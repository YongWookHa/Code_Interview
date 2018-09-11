# http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
# 두번째문제

def read_inputs():
    with open("2-2/2-2_inputs.txt", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line[-1:] is '\n':
            lines[i] = line[:-1]
    return lines
    
def compress(inp):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {alphabet:i for i, alphabet in enumerate(alphabets, 1)}
    def checker(itr, ms):
        nonlocal d
        nonlocal inp
        for i in range(1, ms+1):
            try:
                chk = ''.join(str(x) for x in inp[itr:itr+i])
                if chk in d.keys():
                    result = chk
                else:
                    return result
            except IndexError as e:
                assert("Index Error")
                return result
        return result
                
    result = []
    itr = 0 # where to read in input string
    max_size = 1 # max size of char in dict
    while(itr<len(inp)):
        chk = checker(itr, max_size)
        result.append(d[chk])
        max_size = len(chk) + 1
        d[inp[itr:itr+max_size]] = len(d)+1 
        itr+=len(chk)
    return result
    
if __name__ == "__main__":
    inputs = read_inputs()
    results = list(map(compress, inputs))
    for result in results:
        print(result)