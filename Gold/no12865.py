#12865 평범한 배낭

N, K=map(int, input().split())
bag=[]
for i in range(N):
    W, V = map(int, input().split())
    bag.append([W, V])
bag.sort(key=lambda x:x[0])

value=[0 for i in range(K+1)]
for i in range(N):
    item=bag[i]
    w=item[0]; v=item[1]
    if w>K:
        i=N
        break
    elif w==K:
        if value[K]<v:
            value[K]=v
    else:
        tmp=[0 for j in range(K+1)]
        for j in range(1, K-w+1):
            if value[j]!=0 and value[j+w]<value[j]+v:
                tmp[j+w]=value[j]+v
            if value[w]<v:
                tmp[w]=v
        for j in range(K+1):
            if value[j]<tmp[j]:
                value[j]=tmp[j]
print(max(value))
