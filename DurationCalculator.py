
from datetime import date

print(f'{"Duration Calculator":>68}')
print("\n\'This calculator calculates the duration and time spent asleep between two dates and outputs the result in days, hours, minutes, and seconds\'")
print()

while True:
    try:
        input_today= input("Would you like to use today's date as the 1st input?(Y/N)")
    except ValueError:
        continue 
    if input_today == "Y" or input_today == "y":
        input_date1 = date.today()
        break
    if input_today == "N" or input_today =="n":
        input_day1 = int(input("What is the day of the 1st date?"))
        input_month1 = int(input("What is the month of the 1st date?"))
        input_year1 = int(input("What is the year of the 1st date?"))
        input_date1 = date(input_year1,input_month1,input_day1)
        break
    else:
        print("Invalid Answer")

input_day2 = int(input("\nWhat is the day of the 2nd date?"))
input_month2 = int(input("What is the month of the 2nd date?"))
input_year2 = int(input("What is the year of the 2nd date?"))
input_date2 = date(input_year2,input_month2,input_day2)

input_sleep = float(input("\nHow many hours in average do you sleep a day?"))

duration = abs(input_date1 - input_date2)
Hoursindays = duration.days*24
Minsindays = duration.days*24*60
Secsindays = duration.days*24*60*60 

#Int is cast to a float
Days_asleep = float((input_sleep/24)*duration.days)
Hours_asleep = int(Days_asleep*24)
Mins_asleep = int(Days_asleep*24*60)
Secs_asleep = int(Days_asleep*24*60*60)



print("\nDuration between",input_date1.strftime("%A %d, %B %Y"),"and",input_date2.strftime("%A %d, %B %Y"),":") 
print("  Days   Hours   Minutes     Seconds")
print(f'{duration.days:>6}'
    f'{Hoursindays:>8}'
    f'{Minsindays:>10}'
    f'{Secsindays:>12}')
print("\nAverage time spent asleep :")
print("  Days   Hours   Minutes     Seconds")
print(f'{Days_asleep:>6}'
    f'{Hours_asleep:>8}'
    f'{Mins_asleep:>10}'
    f'{Secs_asleep:>12}')

input("\nPress enter key to exit...")

