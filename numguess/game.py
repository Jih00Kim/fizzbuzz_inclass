import random
user_name = input('Enter your name:')
answer = random.randint(1,100)

# for debugging
print(answer)

guess = int(input('welcome, {}. Guess the nimber! :'.format(user_name)))

#for debugging.
print(answer,guess,type(guess))

if guess == answer:
	print('correct!')
else:
	print('Wrong! The answer is {}.'.format(answer))




