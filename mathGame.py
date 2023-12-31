"""
Day 21 Challenge
Test your family and friends on their multiplication knowledge (or just be really mean to people you know and ask them to work out their multiplication tables for 5,474,000,000....)

Prompt the user by asking for a multiplication table for the number of their choice.
Generate the multiplication table for 1 to 10 times that number and ask each math fact as a question (psst...that's a hint).
If the user gets the math correct, award them a point. If they get it wrong, do not give them any points.
At the end of the 10 rounds, show the user their score out of 10 for how many math facts they got correct.
Why not give users an emoji if they get all 10 math facts correct?
"""

print("Let's play the Math Game!")

num = int(input("Enter the number for Multiplication Table: "))
times = 0

for i in range(1, 4):
    correctAns = i * num
    print(i, "x", num )

    ans = int(input("Enter the answer: "))

    if ans == correctAns:
        print("That's right! You are a genius!")
        times += 1

    else:
        print("Sorry, that's not it. The correct answer is ", correctAns)

    if i == 4:
        print("You got", times, "out of 4 correct!")
        break
