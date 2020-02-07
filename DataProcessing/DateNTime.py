import datetime

'''Date Time Representation'''
'''print('The Date and Time is: ', datetime.datetime.today())

date_today = datetime.date.today()
print(date_today)
print( 'This Year   :', date_today.year)
print( 'This Month    :', date_today.month)
print( 'Month Name:',date_today.strftime('%B'))
print( 'This Week Day    :', date_today.day)
print( 'Week Day Name:',date_today.strftime('%A'))
'''
'''Date Time Arithmetic'''
'''
#Capture the First Date
day1 = datetime.date(2018, 2, 12)
print( 'day1:', day1.ctime())

# Capture the Second Date
day2 = datetime.date(2017, 8, 18)
print( 'day2:', day2.ctime())

# Find the difference between the dates
print( 'Number of Days:', day1-day2)


date_today  = datetime.date.today()

# Create a delta of Four Days
no_of_days = datetime.timedelta(days=4)

# Use Delta for Past Date
before_four_days = date_today - no_of_days
print( 'Before Four Days:', before_four_days)

# Use Delta for future Date
after_four_days = date_today + no_of_days
print( 'After Four Days:', after_four_days)
'''

'''Date Time Comparison'''

date_today  = datetime.date.today()

print( 'Today is: ', date_today)
# Create a delta of Four Days
no_of_days = datetime.timedelta(days=4)

# Use Delta for Past Date
before_four_days = date_today - no_of_days
print( 'Before Four Days:', before_four_days)

after_four_days =  date_today + no_of_days

date1 = datetime.date(2018,4,4)

print( 'date1:',date1)

if date1 == before_four_days :
    print( 'Same Dates')
if date_today > date1:
    print( 'Past Date')
if date1 < after_four_days:
    print( 'Future Date')
