a,b = map(int,input().split())

max_v = max(a,b)

if a == b:
    print(a+b)
else:
    print(2*max_v-1)