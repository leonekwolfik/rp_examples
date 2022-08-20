# age.py

age = int(input("Enter your age: "))

if age >= 0 and age <= 9:
    print("You are a child!")
elif age > 9 and age <= 18:
    print("You are an adolescent!")
elif age > 18 and age <= 65:
    print("You are an adult!")
elif age > 65:
    print("Golden ages!")

