n=int(input("Enter A Value [only odd nos] : "))
for i in range(0,n+1):
    print(' '*(n-i),end=' ')
    for j in range(0,i):
        print('*',end=' ')
    print()
for i in range(n-1,0,-1):
    print(' '*(n-i),end=' ')
    for j in range(0,i):
        print('*',end=' ')
    print()
