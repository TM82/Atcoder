from collections import Counter

N,M = map(int,input().split())

all_likes = []
for i in range(N):
    K,*As = map(int,input().split())
    all_likes.extend(As)

print(len([i for i in Counter(all_likes).values() if i==N]))