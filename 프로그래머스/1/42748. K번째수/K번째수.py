def solution(array, commands):
    answer = [0] * len(commands)
    for i in range(len(commands)):
        lista = sorted(array[commands[i][0]-1:commands[i][1]])
        ind = commands[i][2] - 1
        answer[i] = lista[ind]
    return answer