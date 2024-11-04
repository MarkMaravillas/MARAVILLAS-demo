ROWS = int(input("ENTER NUMBER OF ROWS: "))
num = 1
for x in range(ROWS + 1):
    for y in range (x):
     print(num, "", end="" )
     num += 1
    print()