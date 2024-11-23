import sys
input = sys.stdin.readline

jh = input().rstrip().split('h')[0]
dt = input().rstrip().split('h')[0]

print('no' if len(jh) < len(dt) else 'go')