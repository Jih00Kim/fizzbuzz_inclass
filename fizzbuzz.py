def print_(obj):
	print(obj, end='\t')
for i in range(1,301):
	if i % 15 == 0:
		print_('fizzbuzz')
	elif i % 3 == 0:
		print_('fizz')
	elif i % 5 == 0:
		print_('buzz')
	else:
		print_(i)

print('') 
