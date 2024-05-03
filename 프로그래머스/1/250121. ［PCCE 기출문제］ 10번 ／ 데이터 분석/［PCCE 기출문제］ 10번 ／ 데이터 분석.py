def solution(data, ext, val_ext, sort_by):
    answer = []
    
    dic = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    check = dic[ext]
    sortBy = dic[sort_by]
    
    for i in data:
        if int(i[check]) <= val_ext:
            answer.append(i)
    
    answer.sort(key = lambda x: x[sortBy])
    
    return answer