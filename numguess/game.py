import random
user_name = input('Enter your name:')
answer = random.randint(1,100)

for i in range(0,3):
	if i != 2 :
		guess = int(input('welcome, {}. Guess the number! :'.format(user_name)))
		print(guess)
		if guess == answer:
			print('correct!')
			break
		else:
			print('Wrong! Please try again!')
	elif i == 2:
		guess = int(input('welcome, {}. Guess this is your last chance number! :'.format(user_name)))
		print(guess)
		if guess == answer:
			print('correct!')
			break
		else:
			print('Wrong! The answer is {}.'.format(answer))



