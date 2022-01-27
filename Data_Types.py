# ======================
# Data Types Example
# int - float - bool - str
# list - tuple - dict - set
# ======================
# slicing
x = 'AhmedSelim'
print(x[0:5])
# ----------------------
n = 'my name is ahmed selim'
print(n.title())
print(n.lower())
print(n.upper())
print(n.split(' '))  # split = insert text in list
print(n.replace('is', 'was'))  # replace = change text
print(n.count('a'))  # count = Calculating text frequency
print(n.find('a'))   # Where's the letter?
# ------------------------------
b = [1, 2, 33, 3, 4, 5, 6, 7]
del b[1]  # del =  delete value
print(b)
# ------------------------------
# function built in list
b.reverse()   # Descending order
b.sort()  # Ascending order
b.append(100)   # append = add value end list
b.insert(3, 77)   # insert = add value in A specific place
print(b)
# ------------------------------
w = (1, 2, 33, 3, 4, 5, 6, 7)
e = list(w)   # Change tuple to list and append
e.append(1000)
print(min(e))   # minimum value & max value
# -------------------------------
asd = {1: 'Ahmed', 2: 'mostafa', 3: 'omar'}
print(asd[1])   # print key
del asd[1]
print(asd)
asd.clear()
print(asd)
# ------------------------
q = {1: 'Ahmed', 2: 'mostafa', 3: 'omar'}
for key, value in q.items():
    print(key, value)
# ----------------------------
print(q.values())  # Access value and keys
# ----------------------------
print(q.pop(2))  # Access value
print(q.get(1))  # Access value

# -----------------------------
# Randomisation
import random
name = input("insert name: ")
list_name = name.split(",")
name_ran = random.choice(list_name) #random name in list
print(name_ran)

# =========================================================
# Example of List

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Identify the numbers entered in variables
horzonal = int(position[0]) #2
vertical = int(position[1]) #3

# Grade selection
selcted_row = map[vertical - 1]

#Change the value of the column inside the row to "X"
selcted_row[horzonal - 1] = "😛"


# \n = new line
print(f"{row1}\n{row2}\n{row3}")







