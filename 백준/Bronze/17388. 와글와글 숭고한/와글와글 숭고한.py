S, K, H = map(int, input().split())
if S+K+H>99:
    print("OK")
else:
    min_ = min(S, min(K, H))
    if min_ == S:
        print('Soongsil')
    elif min_ == K:
        print("Korea")
    else:
        print("Hanyang")