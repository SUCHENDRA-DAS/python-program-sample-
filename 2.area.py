def rectangle():
    print("Area Of The  Rectangle : ")
    l=float(input("Enter a value for length : "))
    b=float(input("Enter a value for breadth : "))
    print(f"The Sum Of The Rectangle :{l*b:.2f} ")
def circle():
    print("Area Of The  Circle : ")
    pi=22/7
    r=float(input("Enter a value for radius : "))
    print(f"The Sum Of The Circle :{pi*r*r:.2f} ")
def triangle():
    print("Area Of The  Triangle : ")
    h=float(input("Enter a value for heigth : "))
    b=float(input("Enter a value for base : "))
    print(f"The Sum Of TherTriangle :{0.5*h*b:.2f} ")
def square():
    print("Area Of The  Square : ")
    s=float(input("Enter a value for length : "))
    print(f"The Sum Of The Square :{s*s:.2f} ")
print("1.Area Of The  Rectangle : ")
print("2.Area Of The  Circle : ")
print("3.Area Of The  Triangle : ")
print("4.Area Of The  Square : ")
ch=int(input("Enter A Choice : 1/2/3/4 : "))
if ch==1:
    rectangle()
elif ch==2:
    circle()
elif ch==3:
    triangle()
else:
    square()
