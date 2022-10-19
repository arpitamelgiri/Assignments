'''
#1
num = int(input("enter the number :  "))

if(num%2)==0:
          print(num, "is even number")

else:
    print(num,"is odd number")


#2
celsius = float(input("enter celsius: "))
f= celsius * (9/5) + 32
print("fahrenheit: ", f)


#3
num = float(input("enter number:  "))
meter = num * 2.54
print("Length of the given number is:"{int(meter)},{float(meter)}, meter)


#idyz42y

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

num3 = float(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
   largest = num1

elif (num2 > num1) and (num2 > num3):
   largest = num2

else:
   largest = num3

print("The largest number is",largest)


num = int(input("Enter the number to reverse: "))
rev_num = 0

while num!= 0:
   num1 = num%10
   rev_num = rev_num * 10 + num1
   num = num//10
print("reverse number is: ", rev_num)

''''




























