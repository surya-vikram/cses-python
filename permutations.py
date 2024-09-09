n = int(input())
if n <= 1:
	print(1)
elif n < 4:
	print('NO SOLUTION')
elif n % 2 == 0:
	print(" ".join(map(str, list(range(2, n+1, 2)) + list(range(1, n, 2)))))
else:
	print(" ".join(map(str, list(range(2, n, 2)) + list(range(1, n+1, 2)))))
