import math

def solution(progresses, speeds):
    ptr = 0
    days = math.ceil((100 - progresses[0]) / speeds[0])
    leng = len(progresses) - 1
    answer = []
    
    for i, (p, s) in enumerate(zip(progresses, speeds)):
        if p + s * days < 100:
            answer.append(ptr)
            ptr = 0
            days = math.ceil((100 - p) / s)
            
        ptr += 1
        
        if (i == leng):
            answer.append(ptr)
        
    
    return answer