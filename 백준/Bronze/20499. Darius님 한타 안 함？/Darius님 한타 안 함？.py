str_ = list(map(int, input().split("/")))
if str_[0]+str_[-1] < str_[1] or str_[1] == 0:
    print("hasu")
else:
    print("gosu")