
# Lets Build a Grade Generator
import pyfiglet
font = pyfiglet.figlet_format("GRADE GENERATOR")
print(font)

print("Welcome to the Grade Generator")
print("Please Enter the following details")
print("==================================")

testName = input("Enter the name of the test: ")
maxScore = int(input("Enter the maximum score: "))
pointsGot = int(input("Enter the number of points you got: "))

percent = (pointsGot/maxScore)*100
score = round(percent, 2)

if score >= 90:
  grade = "A+"
elif score >= 80:
  grade = "A"
elif score >= 70:
  grade = "B"
elif score >= 60:
  grade = "C"
elif score >= 50:
  grade = "D"
else:
  grade = "U"

print("You got", score, "% and You are in Grade", grade )