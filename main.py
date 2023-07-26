# a function is a unit of code that perform a task

def calculate_miles_per_gallon(miles_driven, gallon_used):
    mpg = miles_driven / gallon_used
    mpg = round(mpg, 1)
    return mpg


a = calculate_miles_per_gallon(150, 14.56)
print(a)
