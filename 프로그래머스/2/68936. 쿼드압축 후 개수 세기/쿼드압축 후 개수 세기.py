import numpy as np
def solution(arr):
    answer = [0,0]
    if np.sum(arr) == 0:
        return[1,0]
    elif np.sum(arr) == len(arr) * len(arr):
        return[0,1]
        
    def quad(arr):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        suml = [0,0,0,0]
        n = len(arr)
        if n == 1:
            for i in range(2):
                for j in range(2):
                    if arr[i][j] == 0:
                        answer[0] += 1
                    else:
                        answer[1] += 1
        for i in range(n):
            if i < n//2:
                list1.append(arr[i][:n//2])
                suml[0] += sum(arr[i][:n//2])
                list2.append(arr[i][n//2:])
                suml[1] += sum(arr[i][n//2:])
            else:
                list3.append(arr[i][:n//2])
                suml[2] += sum(arr[i][:n//2])
                list4.append(arr[i][n//2:])
                suml[3] += sum(arr[i][n//2:])
                final = [list1,list2,list3,list4]
        if n ==2:
            if sum(suml) == 0:
                return [1,0]
            elif sum(suml) == 4:
                return [0,1]
        for i in range(4):
            if suml[i] == 0:
                answer[0] += 1
            elif suml[i] == (n//2)**2:
                answer[1] += 1
            else:
                quad(final[i])
    
        
    if len(arr) == 1:
        if arr[0] == 1:
            return [1,0]
        else:
            return[0,1]
    quad(arr)
    return answer