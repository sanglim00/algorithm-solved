import sys

def palindrome(str_, left, right):
    if left >= right:
        return -1
    if str_[left] == str_[right]:
        return palindrome(str_, left+1, right-1)
      

while True:
    str_ = sys.stdin.readline().rstrip()
    if str_ == '0': break
    ans = palindrome(str_, 0, len(str_)-1)
    print('yes' if ans else 'no')