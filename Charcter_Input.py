#Create a program that asks the user for their name and age
#Then prints a greeting using that information
#Then tells them how many years they will turn 100
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old.")

year = 2025 - age + 100
print (f"You will be 100 years old in {year}")
#From pythonpractice.org

years = 100 - age
print (f"That means you will be 100 in {years}")
