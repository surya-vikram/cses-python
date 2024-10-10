for _ in range(int(input())):
    row, col = map(int, input().split(' '))
    shape = max(row, col)
    start = (shape-1)**2 + 1
    end = shape**2
    if row<col:
        if shape%2:
            print(end-row+1)
        else:
            print(start+row-1)
    else:
        if shape%2:
            print(start+col-1)
        else:
            print(end-col+1)
