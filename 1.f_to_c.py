def fah_to_cel():
    print("Farhenheit To Celcius Converstion : ")
    farhenheit=float(input("Enter a value for conversion : "))
    celcius=(farhenheit-32)*5/9
    print(f"The Celcius value : {celcius:.2f}")
def cel_to_fah():
    print("Celcius To Farhenheit  Converstion : ")
    celcius=float(input("Enter a value for conversion : "))
    farhenheit=(celcius*9/5)+32
    print(f"The Farhenheit value : {farhenheit:.2f}")
print("1.Farhenheit To Celcius Converstion : ")
print("2.Celcius To Farhenheit  Converstion : ")
ch=int(input("Enter a Value For Choice :1 /2 : "))
if ch==1:
    fah_to_cel()
else:
    cel_to_fah()
