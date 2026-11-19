nc = int(input("Enter number: "))

for x in range (1, 11):
    for y in range(1, nc, 1):
        print(x,"x",y,"=",x*y, end="\t")
    print()