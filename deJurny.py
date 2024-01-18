myPartyList = []
def printList():
    for item in myPartyList:
        print(item)
while True:
    menu = input(""""Choose what I should do:
                 1 - Add a person to the party list
                 2 - Remove a person from the Party list
                 3 - Print the Party List
                 4 - Exit
                 Enter your choice here: """)
    
    if menu == "1":
        item = input("Who should I add to the Party List?: ")
        if item:
            myPartyList.append(item)
        else:
            print("You need to enter a name!")

    elif menu == "2":
        item = input("Who should I remove from the Party List?: ")

        if item in myPartyList:
            myPartyList.remove(item)

        else:

            print(f"{item} is not on the list! ")
    
    elif menu == "3":
        printList()

    elif menu == "4":
        print("Goodbye!")
        break

    else:
        print("That is not a valid choice!")
        print("Please choose 1, or 2, or 3")

    printList()
print("Exiting guest list management system.")



