N = int(input())

company = set()
for _ in range(N):
    name, state = input().rstrip().split()
    if name in company:
        company.remove(name)
    else:
        company.add(name)

for i in sorted(company, reverse=True):
    print(i)