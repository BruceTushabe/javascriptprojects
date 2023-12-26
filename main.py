num1 = int(input("Enter number: "))
num2 = int(input("Enter another: "))

print("Choose Operation:\n"
      "1. Add\n",
      "2. Substract\n",
      "3. Multipy\n",
      "4. Divide\n",
      "5. Modulus\n",
      "6. Exponent\n",

      "Enter Choice here:")

choice = input()

if choice == "1":
    ans = num1 + num2
elif choice == "2":
    ans = num1 -num2
elif choice == "3":
    ans = num1 * num2
elif choice == "4":
    ans = num1 / num2
elif choice == "5":
    ans = num1 % num2
elif choice == "6":
    ans = num1 ** num2
else:
    print("Choice out of scope")

print("The Answer is: ", ans)
