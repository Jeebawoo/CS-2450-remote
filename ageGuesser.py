import random

def main():
	print("Hello, I am going to guess your age!")
	name = input("What is your name? ")
	guess = 50
	step = 25
	while True:
		userInput = input(f"Is your age {guess}? y/higher/lower ")
		if userInput == "y":
			print(f"Your name is {name} and you are {guess} years old.")
			return
		elif userInput == "higher":
			guess += step
		elif userInput == "lower":
			guess -= step
		print("Rats.")
		step = step // 2
main()
