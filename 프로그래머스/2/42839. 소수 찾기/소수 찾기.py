from itertools import permutations

def solution(numbers):
    answer = 0
    perm = []
    flag = True
    
    for i in range(1, len(numbers) + 1):
        for case in set(permutations(numbers, i)):
            perm.append(int("".join(case)))

        
    for num in set(perm):
        flag = True
        if num <= 1: 
            continue
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0: 
                print(num % i)
                flag = False
                break
        if (flag):
            answer += 1
        
    return answer