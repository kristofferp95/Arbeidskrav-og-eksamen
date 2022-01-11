month = int(input(f'Enter a month in the year (for.x: 1 for jan) : '))
year = int(input(f'Enter a year: '))


if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: 
    leap = 1
else: 
    leap = 0

if month == 1: 
    monthName = str("Januar")
    days = 31
elif month == 2 and leap == 1:
    monthName = str("Februar")
    days = 29
elif month == 2 and leap == 0:
    monthName = str("Februar")
    days = 28
elif month == 3: 
    monthName = str("Mars")
    days = 31
elif month == 4: 
    monthName = str("April")
    days = 30
elif month == 5: 
    monthName = str("Mai")
    days = 31
elif month == 6: 
    monthName = str("Juni")
    days = 30
elif month == 7: 
    monthName = str("Juli")
    days = 31
elif month == 8: 
    monthName = str("August")
    days = 31
elif month == 9: 
    monthName = str("September")
    days = 30
elif month == 10: 
    monthName = str("Oktober")
    days = 31
elif month == 11: 
    monthName = str("november")
    days = 30
else:
    monthName = str("desember")
    days = 31
    

print(f'{monthName} {year} has {days} days')

