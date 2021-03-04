def print_(obj):
	print(obj, end='\t')
for i in range(1,301):
	if i % 15 == 0:
		print_('피즈버즈')
	elif i % 3 == 0:
		print_('FIZZ')
	elif i % 5 == 0:
		print_('buzz')
	else:
		print_(i)

print('') 
