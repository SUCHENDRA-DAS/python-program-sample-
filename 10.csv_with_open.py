with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    l=1
    for i in infile:
        if l%2==1:
            outfile.write(i)
        l+=1
