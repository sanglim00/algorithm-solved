N = int(input())
student = []
for _ in range(N):
    lst = list(input().split())
    student.append(lst)

student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
    print(i[0])