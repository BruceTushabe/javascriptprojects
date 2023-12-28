import pyfiglet
font = pyfiglet.figlet_format("LYRICS GAME")
#print(font)

exit = "no"

while True:
    print("Welcome to the Lyrics Game")
    print("See the list of songs below and choose one to play be enter the missing word\n",
          "1-.... gwe omugga ogw'obulamu.\n",
          "2- Great is thy....\n",
          "3- Gow will ..... a way\n",
          "4- There is.... like you\n",
          "5- I will sing of the.....of the Lord\n",
          "6- Blessed be the .....of the Lord\n",)
    
    lyrics = input("Enter your Choice here:").lower()
    
    words = {
    "1": "Yesu",
    "2": "faithfulness",
    "3": "make",
    "4": "none",
    "5": "goodness",
    "6": "name"
    }
    
    if lyrics == "1" in words:
        print("Wow, spot on! Yesu gwe omugga ogw'obulamu")
    elif lyrics == "2" in words:
        print("Oh yeah, the song is Great is thy faithfulness")
    elif lyrics == "3" and words == "1":
        print("Yes, the song is God will make a way")
    elif lyrics == "4" in words:
        print("Yo, There is none like you, it is!")
    elif lyrics == "5" in words:
        print("Thats it!, I will sing of the goodness of the Lord")
    elif lyrics == "6" in words:
            print("Wow! Blessed be the name of the Lord")

    else:
        print("Sorry, let's try again")
    
    if exit == "no":
        print("Do you want to exit?")
        exit = input()
    if exit == "yes":
        break

    
        




