#15649 N과 M (1)

def backtracking(k, m, permutation, check):
    if k==m:
        for num in permutation:
            print(num,end=" ")
        print()
    else:
        for i in range(n):
            if check[i]==0:
                check[i]=1
                permutation[k]=i+1
                backtracking(k+1,m,permutation, check)
                check[i]=0
                permutation[k]=0
    
n, m=map(int,input().split())
check=[0 for i in range(8)]
permutation=[0 for i in range(m)]
backtracking(0,m,permutation,check)
