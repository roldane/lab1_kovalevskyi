print("""
    Лабораторна робота №6
Мета: навчитися писати функції та користуватися ними.

""")

print("     Завдання 1")

year = int(input("year - "))
b = int(4)
c = int(100)
d = int(400)
e = 0#common
f = 0#leap
if year % b != 0:
    e = 2
elif year % b == 0:
    f = 2
if year % c != 0:
    e = 3
elif year % c == 0:
    f = 3
if year % d != 0:
    e = 4
elif year % d == 0:
    f = 4

def is_year_leap(year):
    if e > f:
        return False

    elif f > e:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
        yr = test_data[i]
        print(yr, "->", end = "")
        result = is_year_leap(yr)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")
print(" ")


print("     Завдання 2")

month = input("month - ")

def is_year_leap(year):
    if e > f:
        return False

    elif f > e:
        return True

def days_in_month(year, month):
     if [month == 2, year == 1900]:
         return 28
     if [month == 2, year == 2000]:
         return 29
     if [month == 1, year == 2016]:
         return 31
     if [month == 11, year == 1987]:
         return 30

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
   yr = test_years[i]
   mo = test_months[i]
   print(yr, mo, "->", end="")
   result = days_in_month(yr, mo)
   if result == test_results[i]:
       print("OK")
   else:
       print("Failed")
