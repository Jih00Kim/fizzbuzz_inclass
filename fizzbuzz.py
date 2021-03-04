def print_(obj):
	print(obj, end='\t')
for i in range(1,101):
	if i % 15 == 0:
		print_('fizzbuzz')
	else:
		if i % 3 == 0:
			print_('fizz')
		elif i % 5 == 0:
			print_('buzz')
		else:
			print_(i)

print('') 
