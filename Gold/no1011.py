#1011 Fly me to the Alpha Centauri

n=int(input())
for i in range(n):
    x, y = map(int, input().split())
    length=y-x
    mod=1
    inc=1
    best=1
    while length>best:
        if mod%2==0:
            inc+=1
            best+=inc
        else:
            best+=inc
        mod+=1
    print(mod)
