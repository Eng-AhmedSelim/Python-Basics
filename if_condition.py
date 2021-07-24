# example 1
#===============================================
x = 5
if x == 5:
    print("done")
else:
    print('not done')

#===============================================
#exam 2
#----------------------------------------

if x == 5: print('Welcome') #single if

#===============================================
#exam 3
#---------------------------------------
print('Hello') if x == 5 else print('not dooone')

#===============================================
#Exam 4
#-----------------------------
# Exam in  & not in
employees_staff_1 = {"Ahmed": 1 , "Ali": 2 , "Mohamed" : 3}

if "Ahmed"  in employees_staff_1:
    
    print('found Ahmed')        

else:
    print('not found employee')
#===============================================
#Exam 5
#-------------------------------------
# if all (and) & if any (or)
a = 1
b = 2
c = 3
if all([a == 1 , b == 2 , c == 3]):
    print('done all')
#-------------------------------------------- 

if any([a != 1 , b == 3 , c == 7 ]):
    print(' not found number "any" ') 
else:
     print('found number "any"')


    


















