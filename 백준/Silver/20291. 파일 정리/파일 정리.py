import sys

N = int(sys.stdin.readline())
myDict = {}

for _ in range(N):
    file = sys.stdin.readline().rstrip()
    extension = file.split('.')[1]
    if extension in myDict: myDict[extension] +=1 
    else: myDict[extension] = 1
    
for name, num in sorted(myDict.items()):
    print(name, num)