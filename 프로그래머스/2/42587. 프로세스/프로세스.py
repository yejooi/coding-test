from collections import deque

def solution(priorities, location):
    answer = 0
    pq = deque([(v, i) for i, v in enumerate(priorities)])
    
    while (len(pq)):
        p = pq.popleft()
        if pq and max(pq)[0] > p[0]:
            pq.append(p)
        else:
            answer += 1
            if p[1] == location:
                break
            
    return answer