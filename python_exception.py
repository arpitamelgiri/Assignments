import sys
try:
    print(100/0) #zeroDivision Error will be encountered here.
except:
    print(sys.exc_info()[1]) #This statement will be executed only if exception error found.
else:
    print("No exception occurred!!")
finally:
    print("Run this block of code always") #This statement will be excuted always
