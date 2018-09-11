# http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/ 
# 첫번째 문제

with open('1-1_input.txt', 'r') as inp:
    n = int(inp.readline())
    arr1 = inp.readline().split(' ')
    arr2 = inp.readline().split(' ')
    inp.close()

print('n:', n)
print('arr1:', arr1)
print('arr2:', arr2)

for i in range(n):
    b1 = format(int(arr1[i]),'b').zfill(n)
    b2 = format(int(arr2[i]), 'b').zfill(n)
    
    str = ''
    for j in range(n):
        str += '#' if int(b1[j]) or int(b2[j]) else ' '
    print(str)
        