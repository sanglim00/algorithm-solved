def checkDay(today, plus, date_):
    year = int(date_.split('.')[0])
    month = int(date_.split('.')[1])
    day = int(date_.split('.')[2])
    
    toY = int(today.split('.')[0])
    toM = int(today.split('.')[1])
    toD = int(today.split('.')[2])
    
    sumDate = year * 12 * 28 + month * 28 + day + (plus * 28) - 1
    ansDate = toY * 12 * 28 + toM * 28 + toD
    
    return sumDate < ansDate
        
    
def solution(today, terms, privacies):
    answer = []
    dic = {}
    
    for i in terms:
        key = i.split()[0]
        val = i.split()[1]
        dic[key] = int(val)
    
    for i in range(len(privacies)):
        date_ = privacies[i].split()[0]
        type_ = privacies[i].split()[1]
        
        ans = checkDay(today, dic[type_], date_)
        
        if ans:
            answer.append(i+1)
        
    return answer