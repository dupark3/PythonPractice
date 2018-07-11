import constant
import math
import sys

print(sys.path)

# for loop in range
for i in range(1, 11):
    print(i)
    if i == 5:
        break;

def factorial(num):
    """Function to calculate the factorial of num """
    if num == 0:
        return 1
    return num * factorial(num-1)

print(factorial.__doc__)
print(factorial(5))

# variables are deep copied by default
a = b = c = "google.com"
d = c
d = "apple.com"
print(a)
print(b)
print(c)
print(d)

# constants are in all caps, imported from separate module usually
print(constant.PI)
print(constant.GRAVITY)
print(constant.triple(5))

# lists, slicing
list1= [5, 3, 1, -1, 3]
print(list1[4])
print(list1[2:4])
print(list1[:2])
print(list1[1:])

for i in range(len(list1)):
    print(list1[i])

# data objects are not deep copied!
list2 = list1
print(list2)
print(list1 is list2)
print(list2 is list1)
list2[0] = 10
print(list1 is list2)
print(list1)
print(list2)

last_name = "Park"
name = input("Enter your name: ")
print("Hello,", name, last_name)

# simialr to ?: operator in C
print("yes") if 3 > 4 else print("no")

num1 = float(input("enter your first number to add : "))
num2 = float(input("enter your second number to add : "))
print(num1 + num2)

num3 = float(input("enter a number to square root : "))
print(num3 ** 0.5)

a = float(input("enter the first side of a triangle : " ))
b = float(input("enter the second side of a triangle : " ))
c = float(input("enter the third side of a triangle : " ))
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("%0.2f" %area)

print("My first name is {} and last name is {}".format(name, last_name))
print("First side is {0}, second side is {1}, and third side is {2}".format(a, b, c))

x = 12.34567
print("the value of x is %1.2f" %x)

print(math.pi)


my_list = [1, 5, 7, 2, 1]
my_list.pop()
my_list.append(19)
print(my_list)

my_tuple = (1, 2, 3)
# my_tuple[0] = 3   tuples are immutable
print(my_tuple)

my_set = {1, 3, 2, 2, 5, 5}
print(my_set) # {1, 3, 2, 5} sets have unique elements

my_dict = {"1s2":"He", "1s1":"H"}
print(my_dict["1s1"])
print(my_dict)

# id is like the & operator in C++ to get the address of the pointer
print(id(my_dict))

# functions are objects, and therefore have addresses in memory
function_variable = factorial
print(function_variable(10))


# namespace and scope. variables that are local do not change the global variable 
# unless explicitly declared as global within the local scope
def outer_function():
    global a
    def inner_function():
        a = 15
        print(a)
    inner_function()
    print(a)

a = 100
outer_function()

if (a == 100):
    print("a is 100")
elif (a > 0):
    print("a is positive at least")
else:
    print("a is not 100")

for i in range(len(my_tuple)):
    print(my_tuple[i])

# not only does python have break, it also has continue, allowing you to 
# skip the rest of the loop body. also, loops can have an else statement.
for val in last_name:
    if val == "r":
        continue
    print(val)
else:
    print("end of last name")

def greet(*names):
    for name in names:
        print("Hello, ", name)

greet("Monica", "John", "Jim")
greet(3, 5.3, "James")

my_list = [1, 5, 8, 9, 10, 11, 12]
print("my_list : ", my_list)
new_list = list(filter(lambda x : (x % 2 == 0), my_list))
print(new_list)

new_list2 = list(map(lambda x: (x * 2), new_list))
print(new_list2);
