def print_(obj):
	print(obj,end='\t')
fb_list = ['fizzbuzz' if i%15==0  else 'fizz' if i%3 ==0 else 'buzz' if i%5 ==0 else i for i in range(1,100+1)])
print(fb_list) 
