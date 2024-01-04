# dream
while True:
    def op(a, b):
        print("Please select an Operation: \n"
          "1. Add \n",
          "2. Subtract \n",
          "3. Muiltiply \n",
          "4. Divide")
        
        choice = input("Enter choice: ")
        
        add = a + b
        subtract = a - b
        mutiply = a * b
        divide = a / b

        if  choice == '1':
            return add
        elif choice == '2':
            return subtract
        elif choice == '3':
            return mutiply
        elif choice == '4':
            return divide
        else: 
            print("Invalid input, Try again")
        
        
    num1= int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))

    result = op(num1, num2)
    print("The answer is: ", result)

    repeat = input("Do you want to continue? (yes/no): ")
    if repeat == 'yes':
        continue
    else:
        break