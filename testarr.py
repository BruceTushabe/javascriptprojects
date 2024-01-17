import time

print ("30 DAYS DOWN")

for i in range(1, 20):
    print (f"Day {i} ") 
    thought = input()
    time.sleep(1)
   
    print(f"You thought Day {i} was", thought)

