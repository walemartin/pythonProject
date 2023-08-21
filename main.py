import date_of_birth_calculation as p

print("Voter registration")
fullname = input("Enter full name:    ")

birth_date = input("Please enter your date of birth (DD/MM/YYYY):   ")

result = p.dob(birth_date)
if result < 18 and result > 65:
    print(f"Your age is {result} years. {fullname}, you can now proceed to vote.")
else:
    print(f"Your age is {result} years. {fullname}, you are not eligible to vote.")




