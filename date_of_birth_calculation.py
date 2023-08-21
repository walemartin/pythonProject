
from datetime import datetime


print("date of birth program")

date=datetime.now()
def calculate_age(birth_date, current_date):
    # Calculation
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust for negative differences
    if days < 0:
        months -= 1
        days += get_days_in_month(birth_date.month, birth_date.year)
    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def get_days_in_month(month, year):
    if month < 1 or month > 12:
        raise ValueError("Invalid month value. Month should be between 1 and 12.")

    if not isinstance(year, int) or year < 0:
        raise ValueError("Invalid year value. Year should be a non-negative integer.")

    if month == 2:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29  # Leap year
        else:
            return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:
        return 31


date_str=input("Please enter your date of birth (DD/MM/YYYY): ")
birth_date=datetime.strptime(date_str,"%d/%m/%Y").date()
#age_calulation=(birth_date.year-date.today().year)
#years=age_calulation-birth_date

# Check if the birth date is valid
if birth_date <= date.today().date():
    # Calculate age
    age_years, age_months, age_days = calculate_age(birth_date, date.today())
    print(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")
else:
    print("Please enter a valid date of birth.")