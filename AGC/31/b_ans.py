N = int(input())
C = [int(input()) for i in range(N)]

p = [0 for _ in range((2 * 10**5) + 1)]
dp = [0 for _ in range(N)]
p[C[-1]] = -1
dp[-1] = 1
for i in range(2, N + 1):
    if p[C[-i]] == 0 or p[C[-i]] == -i + 1:
        dp[-i] = dp[-i + 1]
    else:
        dp[-i] = (dp[-i + 1] + dp[p[C[-i]]]) % (10**9 + 7)
    p[C[-i]] = -i
 
ans = dp[0]
print(ans)