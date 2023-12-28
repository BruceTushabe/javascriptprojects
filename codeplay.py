
exit = "no"

while exit == "no":

    animal_sound = input("Please enter the animal to see the sound it makes: ")
    if animal_sound == "dog" or animal_sound == "Dog":
        print("The Dog says Woof Woof")
    elif animal_sound == "cat" or animal_sound == "Cat":
        print("The Cat says Meow Meow")
    elif animal_sound == "cow" or animal_sound == "Cow":
        print("The Cow goes Mooo Mooo")
    elif animal_sound == "duck" or animal_sound == "Duck":
        print(" The Duck bes like Quack Quack")
        print ("So funny, hahahaha")
    elif animal_sound == "goat" or animal_sound == "Goat":
        print("The Goat says Meee Meee")
        print("I just love goats bambi, they are cute!")
    elif animal_sound == "chicken" or animal_sound == "Chicken":
        print("The Chicke says Kookoorookooo")
        print("Ayaaaa... Chicken are yummmmmmmy, hahaa")
    else:
        print("Sorry, that Animal is not in our database")   
    exit = input("Do you want to exit? ")
    
    if exit == "yes" or exit == "Yes":
        print("Thank you for using our program")
        print("Goodbye")
        break
    




                 