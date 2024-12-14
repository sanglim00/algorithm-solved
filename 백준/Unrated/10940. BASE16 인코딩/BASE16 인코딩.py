import base64

S = input().rstrip()
text = S.encode('UTF-8')
result = base64.b16encode(text)
result_S = result.decode('ascii')
print(result_S)