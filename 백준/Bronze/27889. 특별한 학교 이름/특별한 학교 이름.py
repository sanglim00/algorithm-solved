import sys
input = sys.stdin.readline

myDict = {
    'NLCS': "North London Collegiate School",
    'BHA': 'Branksome Hall Asia',
    'KIS': 'Korea International School',
    'SJA': 'St. Johnsbury Academy'
}

now = input().rstrip()
print(myDict[now])