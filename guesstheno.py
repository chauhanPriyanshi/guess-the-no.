import random

print("Welcome to guess the number game. A random number will be generated and you can guess which one it is.")
print("You got three chances.")

number = random.randint(1, 10)
guess = ""  # var to store users guess
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != number and not out_of_guesses:
    if guess_count < guess_limit:
        guess = int(input("Enter your guess: "))
        guess_count += 1
        if guess < number:
            print("Your guess is less than the value . keep trying .")
        elif guess > number:
            print("Your guess is more than the  value . keep trying .")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses. You loose!")
else:
    print("You've won  #cheers 🏆 ")
