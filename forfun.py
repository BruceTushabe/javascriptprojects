import pyfiglet
font = pyfiglet.figlet_format("Let's do this!")
print(font)


print("NOW LET'S PLAY A MATH GAME")

multiplyNum = int(input("Please Enter a number for Multiplication Table: "))

counter = 0

for i in range(1,5):
    correctAns = i * multiplyNum
    print("Now multiply: ", i, "x", multiplyNum)
    answer = int(input("Enter Answer: "))
    if answer == correctAns:
        print("Correct. You are a genius!")
        counter += 1

    else:
        print("Nope! , the right answer is ", correctAns)
        
    if i == 4:
        print("You have scored ", counter, "out of 4")
