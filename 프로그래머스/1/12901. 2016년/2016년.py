def solution(a, b):
    answer = ''
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    total_date = b
    for i in range(a-1):
        total_date += date[i]
    answer = day[total_date % 7]
    return answer