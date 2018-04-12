def max_consecutive_sum(lst):
	if not lst:
		return None
	
	if len(lst) == 1:
		return lst[0]

	curr_max = total = lst[0]

	for i in range(1, len(lst)):

		# if adding the current element to the running total doesn't result
		# in a bigger number, reset the total to the current element.
		if lst[i] > total + lst[i]:
			total = lst[i]
		
		# otherwise, increment total by the current element.
		else:
			total += lst[i]

		# check if total is greater than current max.
		if total > curr_max:
			curr_max = total

	return curr_max

print max_consecutive_sum([-1, 4, -1, 10]) == 13
print max_consecutive_sum([1, 2, 3, 4]) == 10
print max_consecutive_sum([-1, -3, 5, -7]) == 5
print max_consecutive_sum([5, -1, -5, 10]) == 10
print max_consecutive_sum([5, -1, -3, 10]) == 11
print max_consecutive_sum([5, -1, -4, 10]) == 10
print max_consecutive_sum([5, -1, -4, 10, 2]) == 12
print max_consecutive_sum([-1, -1, 14, -10, 12]) == 16