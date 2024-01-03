def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing!")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else:
    print("Yeah, that's great")
    print("So you want a ", ingredient, "cake on a", base, "base with", coating, "on top?")

userIngredient = input("Name the ingredient: ")
userBase = input("Name the base: ")
userCoating = input("Name the coating: ")

whichCake(userIngredient, userBase, userCoating)