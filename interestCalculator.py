import pyfiglet
font = pyfiglet.figlet_format("INTEREST CALCULATOR")
print(font)

loan = int(input("Please enter the Loan Amount: "))
interest = int(input("Please enter the Interest Rate: "))

apr = float(interest/100)


for i in range(10):
    loan += (loan*apr)
    print("Year", i+1, ":", round(loan,2))



    