def solution(s):
    answer = 0
    words =['zero','one','two','three','four','five','six','seven','eight','nine']
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(words)):
        if words[i] in s:
            s = s.replace(words[i],num[i])
    return int(s)