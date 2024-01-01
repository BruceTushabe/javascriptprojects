import random

# Very interesting to discover that random as a module will not work if we have a file named random.py in the same directory 
mynum = random.randint(1, 10)


counter = 0

while True:

    guess = int(input("Please enter your guess: "))

    if guess > mynum:
        print("Your guess is too high. Try again")

        counter += 1

    elif guess < mynum:
        print("Your guess is too low. Try again")

        counter += 1

    elif guess == mynum:
        print("Wow! You guessed right. Try again")
        break
    else:
        print("Input outside the scope. Try again")

print("You got it in ", counter, "triies")



