import numpy as np

N,K = map(int,input().split())
S = [int(i) for i in input()]

split = []
for i in range(1,N):
    if S[i-1] != S[i]:
        split.append(i)

if len(split) <= 1: #全て同じor0001111
    print(N)
else:
    states = [split[0]]
    states.extend([split[i] - split[i-1] for i in range(1,len(split))])
    states.append(N-split[-1])
    print(states)
    if S[0] == 0:
        states = [0].extend(states)
    if S[-1] == 0:
        states.append(0)
    for time in range(K):
        values = [states[i+1] + states[i] + states[i-1] for i in range(1,len(states),2)]
        argmax = np.argmax(values)
        renzoku = states[2*argmax] + states[2*argmax+1] + states[2*argmax+2]
        new_states = [i for i in states[:2*argmax]] + [renzoku] + [i for i in states[2*argmax+2:]]
        states = new_states
        if len(states) == 1:
            break
    print(renzoku)
        