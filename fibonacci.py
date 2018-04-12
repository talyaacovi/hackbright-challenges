def print_fibonacci(n):
	# for i in range(n):
	a = [1, 1]
	for i in range(n - 2):
		a.append(reduce(lambda x, y: x + y, a[-2:]))
	return a

print print_fibonacci(5)


def in_fibonacci(n):
	# for i in range(n):
	a = [1, 1]
	
	while n > a[-1]:
		a.append(reduce(lambda x, y: x + y, a[-2:]))
	
	a = set(a)
	
	if n in a:
		return True
	
	else:
		return False

print in_fibonacci(5)