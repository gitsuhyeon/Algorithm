def solution(data, ext, val_ext, sort_by):
    answer = []
    listname = ["code","date","maximum","remain"]
    e = 0
    s = 0
    k = 0
    for i in range(4):
        if ext == listname[i]:

            e = i
        if sort_by == listname[i]:
            s = i
    
    for j in range(len(data)):
        if data[j][e] < val_ext:
            answer.append(data[j])
            k += 1

    answer.sort(key = lambda x:x[s])
    return answer

def main():
    printing = solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],"date",20300501,"remain")
    print(printing)
        
main()