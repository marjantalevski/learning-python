def drawing(h, v):
    horizontal = " ---"
    vertical = "|   "
    i = 0
    j = 0
    while i < v: 
        print(horizontal * h)
        print(vertical * (h+1))
        i += 1
    print(horizontal * h)

rows = int(input("Enter the number of rows: "))
collumns = int(input("Enter the number of collumns: "))      
drawing(collumns, rows)
