import calendar
year = input("Enter year")
month=input("Enter month")
if month>12:
    print("Please enter correct month")
elif month<12:
    print(calendar.month(year, month))
