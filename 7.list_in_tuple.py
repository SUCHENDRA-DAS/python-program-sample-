lis=list(input("Enter The Value Seperated By Commas For List : ").split(","))
tup=tuple(input("Enter The Value Seperated By Commas For Tuple : ").split(","))
count=0
for i in lis:
    count+=tup.count(i)
print("The Total Repeated Value Count : ",count)
