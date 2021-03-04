def print_(obj):
	print(obj, end='\t')
for i in range(1,101):
	if i % 15 == 0:
		print_('FIZZBUZZ')
	else:
		if i % 3 == 0:
			print_('FIZZ')
		elif i % 5 == 0:
			print_('BUZZ')
		else:
			print_(i)

print('') 
