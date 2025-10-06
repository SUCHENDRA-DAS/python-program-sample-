n=int(input("Enter The Range For Prime No : "))
print("The First Prime Numbers Less Than ",n," : ")
for num in range(2,n):
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
            print(num,end="\t")
