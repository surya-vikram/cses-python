n = int(input())
while n != 1:
    print(n, end=" ")
    n = n // 2 if n % 2 == 0 else n * 3 + 1
print(1)