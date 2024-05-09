def tf(list_par):
    stack =[]
    for char in list_par:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        if char == ")" or char == "}" or char == "]":
            if not stack:
                return False
            cmp = stack.pop()
            if cmp == "(":
                if char == ")":
                    continue
            if cmp == "{":
                if char == "}":
                    continue
            if cmp == "[":
                if char == "]":
                    continue
            else:
                return False
    if not stack:
        return True
                    
                    
def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        l = s[0]
        s = s[1:]
        s.append(l)
        if tf(s):
            answer += 1
    return answer