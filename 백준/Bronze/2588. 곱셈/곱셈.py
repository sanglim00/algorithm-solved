import sys

num = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

print(num*(num2%10))
print(num*((num2%100)//10))
print(num*((num2%1000)//100))
print(num*num2)