def solution(s):
    stack = []
    
    for par in s:
        if par == "(":
            stack.append("(")
        elif len(stack) == 0 and par == ")":
            return False
        elif stack[-1] == "(" and par == ")":
            stack.pop()
            
    return False if len(stack) > 0 else True