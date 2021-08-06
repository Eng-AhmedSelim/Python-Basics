#============================
# Example Function 1
#============================
def sum1(x,y):
    result = x * y
    return result

s = sum1(3,18)
print(s / 2)

print("======================================")

#keyword arguments
# s = sum1(y = 3, x = 18)

#====================================
#Example Fun 2                     ||
#====================================

def sum2(args,*vartuple):
   print(args)
   print(vartuple)
   result = args
   result += sum(vartuple) # sum all numbars in vartuple + valuo result
   return result
# Num 1 in args. 
# Other numbers are collected. 
a = sum2(3,18,22,3,556,78,9)
print(a)

print("======================================")

#=====================================
#Example 3
#=====================================

# lambda function
sum3 = lambda x , y : x * y
print(sum3(3 , 10))


print("======================================")

#===================================
# Example 4
#===================================
w = 0
print(w)
def asum():
    global w # show variable All code "add global"
    w = 3 #local variable
    print(w)
asum()
print(w)

print("======================================")

#===================================
# Example 5 enumerate function
#===================================
name = ["Ahmed","yaser","Ali", "Mohamed","yaseen", "nabil"]

for count , valuo in enumerate(name): # loop on count and valuo in list
    print(count)
    print(valuo)
    if count == 1: # When you get to the count, print out.
        print('in 1--->')
    elif count == 3:
        print('count in ---3')
#===================================
# Example 6 map function
#===================================
v = [1,2,3,4,5,6,7]

def power(n):
    return n*n

b = map(power , v)
print(list(b))
#===================================
# Example 7 zip function
#===================================
names = ['mahmoud','Ahmed','ali']
degre = [47,90,33]
students = zip(names,degre)
print(list(students))

#===================================
# Example 8 filter function
#===================================
r = [1,2,3,4,5,6,7]
def filter_1(n):
    if n > 5:
        return True
    else:
        return False

numbers = filter(filter_1 , r)
print(list(numbers))