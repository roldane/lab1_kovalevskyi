print("     Лабораторна робота №4. Логічні значення. Умовне виконання. Цикли.")
print("Мета: освоїти роботу з логічними змінними, операторами розгалуження та операторами циклів.")
print(" ")


print("     Завдання 1")
print("Використовуючи один з операторів порівняння в Python, напишіть просту дворядкову програму,")
print("яка приймає як вхідні дані параметр n, який є цілим числом, і друкує False, якщо n менше 100 і True, якщо n більше або дорівнює 100.")
print(" ")
print(int(input("Введіть значення: ")) > 100)
print(" ")


print("     Завдання 2")
print("Написати програму визначення найбільшого з двох дійсних чисел, використовуючи констуркцію if-else.")
a = int(input("a = "))
b = int(input("b = "))
if a > b:
    print("a > b")
else:
    a < b
    print("a < b")
print(" ")


print("     Завдання 3")
print("Напишіть програму, яка використовує концепцію умовного виконання, приймає рядок як вхідні дані та...")
c = input("- ")
if c == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif c == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not:", c)
print(" ")


print("     Завдання 4")
income = float(input("Enter the annual income: "))
a = income - 85528
if income < 85528:
    tax = float((income / 100 * 18) - 556.2)
elif income > 85528:
    tax = float(14839.2 + (a / 100 * 32))
if tax < 0:
        tax = 0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
print(" ")


print("     Завдання 5")
a = int(input("year - "))
b = int(4)
c = int(100)
d = int(400)
e = 0#common
f = 0#leap
if a % b != 0:
    e = 2
elif a % b == 0:
    f = 2
if a % c != 0:
    e = 3
elif a % c == 0:
    f = 3
if a % d != 0:
    e = 4
elif a % d == 0:
    f = 4
if e > f:
    print("common year")
elif f < e:
    print("leap year")
if a < 1582:
    print("Not within the Gregorian calendar period.")
print(" ")


print("     Завдання 6")
odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number: "))

# 0 terminates execution.
while number != 777:
    # Check if the number is odd.
    if number % 2 == 1:
        print("Ха-ха! Ви застрягли у моїй петлі!")
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        print("Ха-ха! Ви застрягли у моїй петлі!")
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Молодець, магле! Тепер ти вільний.")
print(" ")


print("     Завдання 7")
import time
for loop in range(5):
    print(loop, "Missisipi")
    time.sleep(1)
print(" ")


print("     Завдання 8")
word = input("access word - ")
while word != "chupacabra":
    word = input("access word - ")
    if word == "chupacabra":
        break
print("You've successfully left the loop.")
print(" ")


print("     Завдання 9")
user_word = input("text a word: ")
for letter in user_word.upper():
    if letter == "A":
        continue
    if letter == "E":
        continue
    if letter == "I":
        continue
    if letter == "O":
        continue
    if letter == "U":
        continue
    elif letter != "A":
        print(letter)
    elif letter != "E":
        print(letter)
    elif letter != "I":
        print(letter)
    elif letter != "O":
        print(letter)
    elif letter != "U":
        print(letter)
print(" ")

print("     Завдання 10")

