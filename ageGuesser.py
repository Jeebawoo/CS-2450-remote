import random

def main()
	print("Hello, I am going to guess your age!")
	name = input("What is your name? ")
	ages = []
	while True:
		guess = random.randint(15, 31)
		while guess in ages:
			guess = random.randint(15, 31)
		if input(f"Is your age {guess}? Y/N ") == "Y":
			print(f"Your name is {name} and you are {guess} years old.")
			return
		else:
			print("Rats.")
			ages.append(guess)

