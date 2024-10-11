import datetime

def solution(age):
    answer = 0
    now = str(datetime.datetime.now()).split('-')

    return int(now[0])-age-1