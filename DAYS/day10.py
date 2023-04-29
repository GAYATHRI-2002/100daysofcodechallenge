print("""one month = 30 0r 31 days
          one year = 365 0r 366 days """)

days = int(input("enter the days in a year : "))
year = 365
leap_year = 366

result = year * 24 *60 *60
leap_year = leap_year * 24 * 60 *60

if days == 365:
  print(" number of seconds in year : ", result)
else:
  print("number of seconds in a leap year : ",leap_year)
