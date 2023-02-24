#2225 합분해
n, k = map(int, input().split())

if k==1:
  print(1)
elif k==2:
  print(n+1)
else:
  l=[(i+1) for i in range(n+1)]
  for i in range(k-2):
    for j in range(1, n+1):
      l[j]+=l[j-1]
  print(l[n]%1000000000)