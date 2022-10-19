# Prime or not

number = int(input("Enter the number: "))
if number > 1:
    for i in range(2,(number//2)+1):
        if(number % i == 0):
            print("it is not prime number ")
            break
    else:
        print("number is prime number")
else:
    print("number is not prime number")



# Python program to display all the prime numbers within an range.

lower = int(input("Enter starting number: "))
upper = int(input("Enter ending number: "))

print("Prime numbers between", lower, "and", upper, "are: ")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
