# ========================
# example loop
# infinite Loop
# while loop ( while = Talamaa )
# ------------------------
x = 1
while x < 10:
    print(x)
    x += 1
print('==================')
# ------------------------
# example 2
# Nested While
# ------------------------
a = 1
while a <= 100:
    x = 1
    print(f'Multiplication table {a}')
    while x <= 10:
        print(a, 'X', x, '=', a*x)
        x += 1
    print('--------------')
    a += 1
# =======================================
# Example For loop (For = Lekol gozee min Kol)
# =======================================
for y in range(1,6):
    print('--------------')
    for x in range(1,11):
        print(y, 'X', x, '=', y*x)
# --------------------------------|
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list_num in c:
    print(list)
    for value in list_num:
        print(value)
# ----------------------------------|
# Control Statement
# break = logout loop
# continue = Skip
# pass = reserve a space
# ----------------------------------|
rows = int(input('Enter Rows: '))
cols = int(input('Enter Cols: '))
for r in range(rows):
    for c in range(cols):
        print('$', end='')
    print()
# ----------------------------------|
# Example
base_size = 20
for r in range(base_size):
    for c in range(r+1):
        print('*', end='')
    print()
# ----------------------------------|
# Example
# Loop through both keys and values, by using the items() method:

thisdict =	{
  "name": "ahmed",
  "age": "29",
  "year": 1992
}
for x, y in thisdict.items():
  print(x, y)

