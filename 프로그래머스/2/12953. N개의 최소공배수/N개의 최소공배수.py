def solution(arr):
    answer = 1
    allarr = arr[0]
    np = arr[0]
    for i in range(1,len(arr)):
        allarr *= arr[i]
        j = 1
        while True:
            if (np *j) % arr[i] == 0:
                np = np * j
                break
            j+= 1
        
    answer = np
    return answer