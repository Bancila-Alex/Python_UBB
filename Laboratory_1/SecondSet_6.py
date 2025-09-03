#Determine a calendar date (as year, month, day) starting from two integer numbers representing the year
#and the day number inside that year (e.g. day number 32 is February 1st).
#Take into account leap years. Do not use Python's inbuilt date/time functions.

def leap_year(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True
    return False

def determine_the_date(years, num, months):
    while num:
        for i in months:
            if months[i] < num:
                num -= months[i]
            else:
                return years, num, i
        years += 1

if __name__ == "__main__":
    all_months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    number = int(input("Give the number you want to determine as a date: "))
    year = int(input("Give the year: "))
    if leap_year(year):
        all_months['February'] += 1
    new_year, number, month = determine_the_date(year, number, all_months)
    if new_year > year:
        print(number, month, new_year)
    else:
        print(number, month)