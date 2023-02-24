#1256 사전

n, m, k = map(int, input().split())
r=min(n,m)
coeff=[[0], [1]]
if k==1:
    print("a"*n+"z"*m)
else:
    for i in range(2,n+m+1):
        tmp=coeff[i-1][:]
        R=min(r,i)
        row=[]
        for j in range(R+1):
            if j==0 or j==i:
                row.append(1)
            elif j==1 or j==i-1:
                row.append(i)
            else:
                row.append(tmp[j-1]+tmp[j])
        coeff.append(row)

    ans=""
    r=min(n, m)
    if k>coeff[n+m][r]:
        print(-1)
    else:
        while k>0 and n>0 and m>0:
            r=min(n-1, m)
            tmp=coeff[(n-1)+m][r]
    
            if k<=tmp:
                ans+="a"; n-=1

            else:
                ans+="z"; m-=1
                k-=tmp

        ans+="a"*n+"z"*m
        print(ans)
