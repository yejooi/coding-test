def solution(citations):
    citations.sort(reverse = True)
    result = 0
    
    for i, c in enumerate(citations):
        if c >= i + 1:
            result = i + 1
        else:
            break
            
    return result