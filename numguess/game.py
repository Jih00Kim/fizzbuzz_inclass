import random
user_name = input('Enter your name:')
answer = random.randint(1,100)

# for debugging
print(answer)
for i in range(3):
	if i != 2 :
		guess = int(input('welcome, {}. Guess the nimber! :'.format(user_name)))

#for debugging.
		print(answer,guess)

		if guess == answer:
			print('correct!')
		else:
			print('Wrong! Please try again!')
	elif i == 2:
		print('Wrong! The answer is {}.'.format(answer))



