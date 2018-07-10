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