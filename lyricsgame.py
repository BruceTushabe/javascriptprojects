import pyfiglet
font = pyfiglet.figlet_format("LYRICS GAME")
print(font)

exit = "no"

while True:
    lyrics = input("..... gwe omugga ogw'obulamu.\n"
                    "Enter the missing word: ")
    if lyrics == "Yesu" or lyrics == "yesu":
        print("Wow, spot on! You are a genius")

    else:
        print("Sorry, let's try again")

    if lyrics == "Yesu" or lyrics == "yesu":
        break
        
    if exit == "no":
        print("Do you want to exit?")
        exit = input()
    if exit == "yes":
        break

    
        




