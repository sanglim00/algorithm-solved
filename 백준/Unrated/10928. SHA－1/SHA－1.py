import hashlib

S = input().rstrip()
text = S.encode('utf-8')
md5 = hashlib.new('sha1')
md5.update(text)
result = md5.hexdigest()
print(result)