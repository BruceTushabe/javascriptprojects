import pyfiglet
font = pyfiglet.figlet_format("GUESS NUMBER GAME")
print(font)

print("Yoooo! Let's play the Numbers Game!")

num = 6 # The number to be guessed
attempts = 1 # Number of attempts

while True:
    guess = int(input("Enter your Guess: "))

    if guess > num:
        print("Your guess is too high. Let's try again: ")
        attempts += 1  
    elif guess < num:
        print("Your guess is too low. Let's give it another shot: ")
        attempts += 1
    elif guess == num:
        print("Wow, you got it right!. The actual number is", num)
        print("What a Genius! You got it in ", attempts, "attempts")
        break
    else:
        print("Invalid input. Thanks for Trying")
        exit()