# http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
# 일곱번째 문제

def read_inputs():
    with open('1-7/1-7_input.txt', 'r') as f:
        lines = f.readlines()
    inp = []
    for line in lines:
        inp.append(line[:-1].split(', '))
    return inp

class logs:
    def __init__(self, inp):
        time = inp[11:23]
        self.end_time = int(time[:2])*3600000 + int(time[3:5])*60000 + int(time[6:8])*1000 + int(time[9:])
        duration = int(float(inp[24:-1])*1000)
        self.start_time = self.end_time - duration + 1
        
    def set_start_time(self, time): # for window
        self.start_time = time
        self.end_time = time + 999
        
    def is_overlap(self, compare):
        if self.start_time < compare.start_time and compare.start_time <= self.end_time:
            return True
        elif compare.start_time < self.start_time and self.start_time <= compare.end_time:
            return True
        elif self.start_time == compare.start_time:
            return True
        
        return False
        
def solution(inputs):
    log_list = []
    for inp in inputs:
        log_element = logs(inp)
        log_list.append(log_element)
    sorted(log_list, key=lambda log: log.start_time)
    
    window = logs(inputs[0][:24]+'1s')
    
    result = 0
    for log in log_list:
        temp = 0
        window.set_start_time(log.start_time)
        for x in log_list:
            if window.is_overlap(x):
                temp += 1
        if result < temp:
            result = temp
        
        temp = 0   
        window.set_start_time(log.end_time)
        for x in log_list:
            if window.is_overlap(x):
                temp += 1
        if result < temp:
            result = temp
            
    return result 
            
        

if __name__ == '__main__':
    inp = read_inputs()
    results = list(map(solution, inp))
    
    for result in results:
        print(result)