# Create a program to create a following form inputs as CLI inputs 

name = input("Enter your name: ")
DOB = input ("Enter your birthdate in dd/mm/yy: ")
age = int(input("Enter your age: "))
hobby = list(map(str, input("Enter your hobby: ").strip().split(' ')))

print(name, DOB, age, hobby)