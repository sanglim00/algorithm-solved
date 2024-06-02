import sys

def checkStr(str_, i, j):
    ans = 1

    while i < j:
        if str_[i] == str_[j]:
            i+=1
            j-=1
        else:
            ans = 2
            break

    return ans

if __name__=='__main__':
    t = int(sys.stdin.readline())

    for _ in range(t):
        str_ = sys.stdin.readline().strip()

        i, j = 0, len(str_) - 1

        ans = 0
        check = False
        
        while i < j:
            if str_[i] == str_[j]:
                i+=1
                j-=1
            elif (str_[i] == str_[j-1] or str_[i+1] == str_[j]) and check == False:
                if str_[i] == str_[j-1] and str_[i+1] == str_[j]:
                    a = checkStr(str_, i+1, j)
                    b = checkStr(str_, i, j-1)
                    ans = min(a, b)
                    break
                elif str_[i+1] == str_[j]:
                    i += 1
                    ans = 1
                elif str_[i] == str_[j-1]:
                    j -= 1
                    ans = 1
                check = True
            else: 
                ans = 2
                break

        print(ans)
