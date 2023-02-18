#9663 N-Queen

def backtracking(count, n, where, chess):
    possible=0

    if count==0:
        for i in range(n):
            chess[i]=True
            where[0]=i
            possible+=backtracking(count+1, n, where, chess)
            chess[i]=False
            where[0]=-1
        return possible
  
    elif count<=n-1:
        for i in range(n):
            if chess[i]==False:
                k=1;
                while count-k>=0:
                    if abs(where[count-k]-i)/k==1:
                        break
                    else:
                        k+=1
                if k>count:
                    chess[i]=True
                    where[count]=i
                    possible+=backtracking(count+1, n, where, chess)
                    chess[i]=False
                    where[count]=-1
        return possible

    else:
        return 1
        
n=int(input())
where=[-1 for i in range(n)]
chess=[False for i in range(n)]
possible=backtracking(0,n, where, chess)
print(possible)
