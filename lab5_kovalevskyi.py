print(
    """"
    Лабораторна робота №5
Мета: освоїти роботу зі списками.

     Завдання 1
 """)

list = [1, 2, int(input("num - ")), 4, 5]
list.pop()
print("список - ", list, "довжина - ", len(list))
print(" ")


print("     Завдання 2")
print("Несортоване:")
list = [1, 5, 3, 4, 2, 6]
print(list)
print("Відсортоване:")
j = 1
while j < len(list):
    k = 0
    while k < (len(list) - 1):
        if list[k] > list[k + 1]:
            list[k], list[k + 1] = list[k + 1], list[k]
        k += 1
    j += 1

print(list)
print(" ")


print("     Завдання 3")
list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
j = 1
while j < len(list):
    k = 0
    while k < (len(list) - 1):
        if list[k] > list[k + 1]:
            list[k], list[k + 1] = list[k + 1], list[k]
        k += 1
    j += 1
r = [list[0]]
i = 1
j = 0
while i < len(list):
    if r[j] != list[i]:
        r.append(list[i])
        j += 1
    i += 1
print("The list with unique elements only:")
print(r)
print(" ")


print("     Завдання 4")

print("A B C D E F G H")
board = [["T", "_", "_", "_", "_", "_", "_", "T", 1],
         ["_", "_", "_", "_", "_", "_", "_", "_", 2],
         ["_", "_", "_", "_", "_", "_", "_", "_", 3],
         ["_", "_", "_", "_", "_", "_", "_", "_", 4],
         ["_", "_", "_", "_", "_", "_", "_", "_", 5],
         ["_", "_", "_", "_", "_", "_", "_", "_", 6],
         ["_", "_", "_", "_", "_", "_", "_", "_", 7],
         ["T", "_", "_", "_", "_", "_", "_", "T", 8]]

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end = " ")
    print()
print(" ")

print("Висновок: освоїв роботу зі списками.")