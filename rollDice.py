import random

def roll_dice(num_sides):
 """Rolls a single die with the specified number of sides and returns the result."""
 return random.randint(1, num_sides)

def generate_health_stats():
 """Generates health stats by rolling a 6-sided and 8-sided die and multiplying them."""
 roll_6 = roll_dice(6)
 roll_8 = roll_dice(8)
 health = roll_6 * roll_8
 return health

while True:
 health = generate_health_stats()
 print("Character's health stats:", health)

 choice = input("Generate stats for another character? (y/n): ")
 if choice.lower() != 'y':
   break

print("Exiting character creation.")
