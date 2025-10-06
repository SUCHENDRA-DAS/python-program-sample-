def fact(n):
    return 1 if n==0 else n*fact(n-1)
n=int(input("Enter A Value For Factorial : "))
print("The Factorial Of ",n,"is : ",fact(n))
