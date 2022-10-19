import sys

try:
    x = int(input("Enter first Number: "))
    if x > 50:
        raise ValueError(x)

except:
    print(sys.exc_info()[0])

x = -1

if x < 0:
    raise Exception("No, Number below zero is allowed!")

x= "Hello python"

if not type(x) is int:
    raise TypeError("Only integers are Allowed")
