#1987 알파벳

import sys

global A
A=0

def backtracking(alphabet, R, C, i, j, count, used, visited):
    isused=False
    if i-1>=0:
        if visited[i-1][j]==0:
            a=alphabet[i-1][j]; num=ord(a)-65
            if used[num]==0:
                isused=True
                visited[i-1][j]=1; used[num]=1
                backtracking(alphabet, R, C, i-1, j, count+1, used, visited)
                visited[i-1][j]=0; used[num]=0
    if i+1<R:
        if visited[i+1][j]==0:
            a=alphabet[i+1][j]; num=ord(a)-65
            if used[num]==0:
                isused=True    
                visited[i+1][j]=1; used[num]=1
                backtracking(alphabet, R, C, i+1, j, count+1, used, visited)
                visited[i+1][j]=0; used[num]=0
    if j-1>=0:
        if visited[i][j-1]==0:
            a=alphabet[i][j-1]; num=ord(a)-65
            if used[num]==0:
                isused=True
                visited[i][j-1]=1; used[num]=1
                backtracking(alphabet, R, C, i, j-1, count+1, used, visited)
                visited[i][j-1]=0; used[num]=0
    if j+1<C:
        if visited[i][j+1]==0:
            a=alphabet[i][j+1]; num=ord(a)-65
            if used[num]==0:
                isused=True
                visited[i][j+1]=1; used[num]=1
                backtracking(alphabet, R, C, i, j+1, count+1, used, visited)
                visited[i][j+1]=0; used[num]=0

    if isused==False:
        global A
        if A<count:
            A=count

R, C = map(int, input().split())
alphabet=[]; used=[0 for i in range(36)]; visited=[[0 for i in range(C)] for j in range(R)]
for i in range(R):
    row=sys.stdin.readline().strip()
    alphabet.append(row)

a=alphabet[0][0]; num=ord(a)-65; used[num]=1; visited[0][0]=1
backtracking(alphabet, R, C, 0, 0, 1, used, visited)
print(A)