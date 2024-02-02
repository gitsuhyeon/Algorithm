def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n
    matrix =[[]] * n
    for i in range(n):
        matrix[i] = [0] * n
    for i in range(len(report)):
        nr = report[i].split()
        er = id_list.index(nr[0])
        ee = id_list.index(nr[1])
        if matrix[ee][er] == 0:
            matrix[ee][er] += 1
    for i in range(n):
        if sum(matrix[i]) >= k:
            for j in range(n):
                answer[j] += matrix[i][j]
        
    
    return answer