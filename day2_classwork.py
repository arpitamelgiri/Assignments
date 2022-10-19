
#string

string = 'Hellow World'
string1 = "Hellow world !"
string2 = """Hi we are learning
basic python"""
string3 = '''we have learnt  1. Basic program  2. Control flow '''


print(string)
print(string1)
print(string2)
print(string3)
print(len(string))
print("2nd letter",string1[2])
print("last letter",string1[-1])
print(string*2)
print(string2 + string3)
print("First 4 letters of string", string1[4])
print("Enter string from 4th position",string[4:])
print("string between 2nd and 4th position", string2[2:9])
print("reverse the string", string1[::-1])
print("find position of W from string",string.find("W"))





#LIST
'''

fruits = ["apple", "kiwi", "grapes", "orange", "pineapple"]
print(fruits)
print(fruits[2])

fruits[2]="papaya"
len(fruits)
for i,fruits in enumerate(fruits):
    print(i+1,")",fruits)

fruits.append("banana")
print(fruits)
fruits.insert(2,"guava")
print(fruits)
fruits.reverse()
print(fruits)
seasonal_fruits = ["mango","dragon fruit"]
fruits.extend(seasonal_fruits)
print(fruits)
print(fruits.pop(1))
print(fruits)
fruits.remove("grapes")
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

print("first 2 fruits", fruits[ :2])
print(fruits[3:5])
      
fruits[ :2]
print(fruits)

'''
'''
#TUPLE

cities = ("bangalore", "pune" , "mumbai")
print(cities)
print(type(cities))

'''

#DICTIONARY

weekdays = {1:"sun", 2:"mon", 3:"tue", 4:"wed", 5:"thur", 6:"fri", 7:"sat"}
print(type(weekdays))

print(type(weekdays),weekdays)
print(weekdays[1])
for key in weekdays:
    print("Key = "+str(key) + ", value=" + weekdays[key])
          
weekdays[1] = "Holiday"
print(weekdays)
del weekdays[7]
print(weekdays)

























      














