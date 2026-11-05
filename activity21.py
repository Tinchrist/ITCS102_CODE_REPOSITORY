sum = 0

tuloy = True

while tuloy == True:
    x = int(input("Please enter a number: "))

    if x == 0:
        print("Loop is terminated.")
        print("Total of all number is, ", sum)
        break

    else:
        print("Continue the loop.")
        sum += x
        print("Current total is: ", sum)
        continue