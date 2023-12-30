import pyfiglet
pont = pyfiglet.figlet_format("LIST GENERATOR")
print(pont)

start = int(input("Start here: "))
end = int(input("End here: "))
increment = int(input("Increment between values: "))

print("Let the game begin")
print("----------------------------------------")

for i in  range(start, end, increment):
    print(i)
