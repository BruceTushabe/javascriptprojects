import os, time

listOfEmails = []

def emailPrint():
  os.system("clear")
  print("List of Emails")
  print()
  counter = 1
  for emails in listOfEmails:
    print(f"{counter}: {emails}")
    counter += 1
  time.sleep(1)

def spamPrint(max):
  for i in range(0, max):
    print(f"""Email {i+1}
    
Dear {listOfEmails[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.
Love and hugs,

Yooo Spammington """
)
    time.sleep(1)
    os.system("clear")
    

while True:

  print("SPAMMER Inc")

  if len(listOfEmails) == 0:
    print("list is empty")

  lis = input("1. Add email\n2. Remove email\n3. Show emails\n4. Get SPAMMING\n")
  if lis == "1":
    email = input("Email: ")
    listOfEmails.append(email)
  elif lis == "2":
    email = input("Email: ")
    if email in listOfEmails:
      listOfEmails.remove(email)
      
  elif lis == "3":
    emailPrint()
    
  elif list == "4":
    spamPrint(10)

  time.sleep(1)
  os.system("clear")
    
  
    
    