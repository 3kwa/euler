def is_leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    if year % 4 == 0:
        return True
    return False

def days_in_feb(year):
    return 29 if is_leap_year(year) else 28

def days_in_month(year):
    return (31, days_in_feb(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

WEEK = ('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')

def first_of_month(year, first_of_year):
    acc = 0
    result = [first_of_year]
    for days in days_in_month(year):
        acc += days
        result.append( WEEK[ (acc % 7 + WEEK.index(first_of_year)) % 7 ])
    return result[:-1], result[-1]


first_days_for_year_1900, first_day_1901 = first_of_month(1900, 'Mo')

all_ = []
first_ = first_day_1901
for year in range(1901, 2001):
    for_year, first_ = first_of_month(year, first_)
    all_.extend(for_year)

print sum(1 for first in all_ if first == 'Su')
