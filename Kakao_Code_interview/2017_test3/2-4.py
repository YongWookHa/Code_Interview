# http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
# 네번째문제

import re
import time

def read_input():
    with open("2-4/2-4_inputs.txt", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = re.findall('"(.+?)"', line)
    return lines

class info():
    def __init__(self, li):
        st = li[0] # start_time
        st = int(st[:2])*60+int(st[3:])
        et = li[1] # end_time
        et = int(et[:2])*60+int(et[3:])
        self.duration = et - st
        self.name = li[2]
        self.score = self.set_score(li[3], self.duration) # 악보
        self.match = False
        
    def set_score(self, score, duration):
        score = re.findall('.#?', score) # 플랫 포함 음계를 한개 취급
        result = "".join(score[i%len(score)] for i in range(duration))
        return result             
    
def music_just_now(inputs):
    m = inputs[0]
    musicinfos = [infos.split(',') for infos in inputs[1:]]
    matched = []
    for i, music in enumerate(musicinfos):
        musicinfos[i] = info(music)
        
    for music in musicinfos:
        match_real = re.findall(m, music.score) # 예제 3번 예외
        match_fake = re.findall(m+'#', music.score)
        if len(match_real)-len(match_fake) != 0:
            music.match = True
            matched.append(music)
    if matched:
        max_duration, result = (0, 0)
        for music in matched:
            if music.duration > max_duration:
                max_duration = music.duration
                result = music
        return result.name
    else:
        return '(None)'
    
if __name__=="__main__":
    start_time = time.time()
    inputs = read_input()
    print("inputs: ", inputs)
    results = list(map(music_just_now, inputs))
    for result in results:
        print(result)
    print(time.time()-start_time)
    
        