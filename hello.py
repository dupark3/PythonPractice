import constant
# python testing

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

print(constant.PI)
print(constant.GRAVITY)
print(constant.triple(5))