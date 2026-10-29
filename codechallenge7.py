s = int(input('Input diamond size here: '))

for i in range(1, s + 1):
    print(" " * (s - i) + "* " * i)

for i in range(s - 1, 0, -1):
    print(" " * (s - i) + "* " * i)

