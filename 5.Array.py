n=int(input("Enter A Value For Range Of Array : "))
no=[]
a=[]
b=[]
even,odd=0,0
no=[int(input("Enter A value : ")) for i in range(n)]
for i in no:
    if i%2==0:
        even+=1
        a.append(i)
    else:
        odd+=1
        b.append(i)
print("The Even Count Is : ",even)
print("The Even Nos : ",a)
print("The Odd Count Is : ",odd)
print("The Odd Nos : ",b)
