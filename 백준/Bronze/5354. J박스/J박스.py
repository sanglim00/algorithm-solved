N = int(input())
for i in range(N):
    num = int(input())
    if num == 1:
        print('#')
        print()
        continue
    elif num == 0:
        continue
    print('#'*num)
    for _ in range(num-2):
        print('#', end='')
        print('J'*(num-2), end='')
        print('#')
    print('#'*num)
    if N != i +1: 
        print()
