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
# Example 5
#===================================