deg,dis = map(int,input().split())
dirs = "N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW".split()
Dir = dirs[((deg*10+1125)//2250)%16]
v=list(map(int, "25 155 335 545 795 1075 1385 1715 2075 2445 2845 3265".split()))
v=[i*60/100 for i in v] #風程に直す

w = 0
for i in v:
    if dis >= i:
        w += 1

if w == 0:
    Dir = "C"

print(Dir,w)