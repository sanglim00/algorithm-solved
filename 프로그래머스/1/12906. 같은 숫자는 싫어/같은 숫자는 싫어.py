def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not arr[i] in answer:
            answer.append(arr[i])
        elif answer[len(answer)-1] != arr[i]:
            answer.append(arr[i])
    return answer