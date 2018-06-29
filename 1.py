print("Question1")
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except Exception as e:
    print("Exception: ",e)
print('*'*10)
print('\n')

print("Question2")
l=[1,2,3]
try:
    print(l[3])
except Exception as e:
    print("Exception: ",e)
print('*'*10)
print('\n')

print("Question3")
try:
    raise NameError("Hi there")  
except NameError:
    print("An exception")
    raise
#OUTPUT:
'''An exception
Traceback (most recent call last):
  File "C:\git\Assignment13\1.py", line 23, in <module>
    raise NameError("Hi there")
NameError: Hi there'''
print('*'*10)
print('\n')

print("Question4")
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
#OUTPUT:
'''-5.0
a/b result in 0 '''
print('*'*10)
print('\n')

print("Question5")
try :
    from math import minus
except ImportError as er1:
    print("EXCEPTION OCCURED")
    print(er1)
    print('\n')
try:
    li = [0,1,3,str]
    print(li[5])
except IndexError as er2:
    print("EXCEPTION OCCURED")
    print(er2)
    print('\n')
try:
    val = int("meenal")
except ValueError as er3:
    print("EXCEPTION OCCURED")
    print(er3)
    print('\n')
print('*'*10)
print('\n')

print("Question6")
class AgeTooSmallError(Exception):
    "Raised when age is less than 18"

age = 18

while True:
    try:

        ip_age = int(input("enter the age:"))
        if (ip_age<age):
            raise AgeTooSmallError
        break
    except  AgeTooSmallError:
        print("WARNING : Age must not be less than 18")
        print()
print("It's perfect")
        

