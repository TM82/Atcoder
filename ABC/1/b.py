m = int(input())
d = m / 1000

if d < 0.1:
    vv = 0
elif d <= 5:
    vv = 10 * d
elif (d >= 6) & (d <= 30):
    vv = d + 50
elif (d >= 35) & (d <= 70):
    vv = (d-30)/5 + 80
else:
    vv = 89

print(str(int(vv)).zfill(2))