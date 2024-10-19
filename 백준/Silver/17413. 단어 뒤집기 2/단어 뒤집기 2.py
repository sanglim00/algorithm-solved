str_ = input().rstrip()

ans = ''
st = []
reverse_ = False
for i in str_:
    if reverse_ and i != '>':
        ans += i
    elif i == '<':
        while st: ans += st.pop()
        ans += i
        reverse_ = True
    elif i == '>':
        ans += i
        reverse_ = False
    elif i == ' ':
        while st: ans += st.pop()
        ans += i
    else:
        st.append(i)
 
while st: ans += st.pop()
print(ans)