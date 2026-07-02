from collections import deque

def solution(priorities, location):
    cnt = 0
    priorities = deque(priorities)
    
    while (len(priorities) > 0):
        p = priorities.popleft()
        if priorities and max(priorities) > p:
            priorities.append(p)
            if location == 0:
                location = len(priorities)
        else:
            cnt += 1
            if location == 0:
                return cnt
            
        location -= 1