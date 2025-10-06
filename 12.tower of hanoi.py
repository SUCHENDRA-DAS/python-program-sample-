n=int(input("Enter The Number Of Disks:"))
def hanoi(n,source,target,auxiliary):
    if n==1:
        print("Move disk 1 from",source,"to",target)
        return
    hanoi(n-1,source,auxiliary,target)
    print(f"Move disk {n} form {source} to {target}")
    hanoi(n-1,auxiliary,target,source)
hanoi(n,"A","B","C")
