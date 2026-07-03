def solution(numbers):
    answer = ""
    strings = list(map(str, numbers))
    for s in sorted(strings, key=lambda x: x * 3, reverse=True):
        answer += s
        
    if (answer[0] == '0'):
        answer = str(int(answer))
        
    return answer