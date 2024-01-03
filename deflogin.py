def login():
  while True:
    name = input("What is your name: ")
    passwd = input("What is your password: ")
    if name == "admin" and passwd == "admin":
      print("Welcome Admin")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue

print("REPLIT LOGIN SYSTEM")
login()