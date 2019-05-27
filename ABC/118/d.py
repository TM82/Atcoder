N,M = map(int,input().split())
As = list(map(int,input().split()))

#Asの中に同じマッチ棒の数の数字があれば最大のものしか考えない
all_num_match = sorted([(i,j) for i,j in zip(range(1,10),[2,5,5,4,5,6,3,7,6]) if i in As],key=lambda x:(-x[1],-x[0]))
match_num = {}
for tup in all_num_match:
    if tup[1] not in match_num:
        match_num[tup[1]] = tup[0]

#N本のマッチをちょうど使い切る中で数字をたくさん選びたい
#再帰を使って、割り切れたときに戻っていくアルゴリズムにした
def choice_matches(N,matches):
    if matches:
        min_match = matches[0]
        if N % min_match == 0:
            return {min_match: int(N/min_match)}
        else:
            max_digit = N // min_match
            i = max_digit - 1
            while True:
                sub_dic = choice_matches(N - min_match * i,matches[1:])
                if sub_dic:
                    dic = {min_match:i}
                    dic.update(sub_dic)
                    return dic
                else:
                    i -= 1
                    if i < 0:
                        return {}
    else:
        return {}

matches = sorted(list(match_num.keys()))
use_matches = choice_matches(N,matches)
use_matches = sorted([(i,j) for i,j in use_matches.items()],key=lambda x:x[0]) #(マッチの本数,数字の数)

#一番大きい数字から左に並べていく
numbers = sorted([match_num[i] for i,j in use_matches for k in range(j)],reverse=True)
numbers = ''.join([str(i) for i in numbers])
print(numbers)
