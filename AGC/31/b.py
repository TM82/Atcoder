from collections import defaultdict

N = int(input())

dic = defaultdict(list)
for i in range(N):
    c = input()
    dic[c].append(i)

#列内の連続した数字をくっつける
def merge_list(l):
    l = sorted(l,reverse=True)
    for i in range(len(l)-1):
        if l[i] - l[i+1] == 1:
            l[i] = l[i+1]
    return sorted(list(set(l)))

#辞書内の長さが2以上のkeyを返す
def check_end(dic):
    return [key for key,value in dic.items() if len(value) > 1]

#再帰っぽく処理する
def main(dic):
    keys = check_end(dic)
    if keys:
        return

for key in dic:
    dic[key] = merge_list(dic[key])

#2つ以上要素がある数字を選ぶ
while(True):
    keys = check_end(dic)
    if not keys:
        break #2つ以上要素がなくなったらbreak
    