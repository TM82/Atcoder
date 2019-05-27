from collections import Counter

N = int(input())
S = [i for i in input()]
NN = 10**9 + 7

values = list(Counter(S).values())
values = [i+1 for i in values]
X = 1
for i in values:
    X *= i

print((X-1) % NN)