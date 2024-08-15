import sys

N = sys.stdin.readline().rstrip()
myDict = {}

for i in range(10): myDict[f'{i}'] = 0
for i in range(len(N)): myDict[N[i]] += 1

ans = 0 
for k, v in myDict.items(): ans += v

if ans-myDict['6']-myDict['9'] != 0:

    check = (myDict['6'] + myDict['9'])//2 if (myDict['6'] + myDict['9'])%2==0 else (myDict['6'] + myDict['9'])//2+1
    myDict['6'] = check
    myDict['9'] = check

    ans = [v for k,v in myDict.items() if max(myDict.values()) == v]
    print(ans[0])

else: 
    if ans == myDict['9']: print(myDict['9']//2 if myDict['9'] %2 ==0 else myDict['9']//2+1)
    elif ans == myDict['6']: print(myDict['6']//2 if myDict['6'] %2 ==0 else myDict['6']//2+1)
    else: 
        check = (myDict['6'] + myDict['9'])//2 if (myDict['6'] + myDict['9'])%2==0 else (myDict['6'] + myDict['9'])//2+1
        print(min(max(myDict['6'], myDict['9']), check))