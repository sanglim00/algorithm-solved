import base64

S = input().rstrip()
result = base64.b16decode(S)
result_S = result.decode('ascii')
print(result_S)