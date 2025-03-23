T = int(input())

for _ in range(T):
    num = int(input())
    bin_ = str(bin(num))
    for i in range(len(bin_)-1, -1, -1):
        if bin_[i] == '1':
            print(len(bin_)-1-i, end=" ")
    print()