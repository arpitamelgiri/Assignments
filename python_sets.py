
#Union
A = {1,2,3,4,5,6,7}
B = {6,7,8,9,10}
C = {8,9,10,11,12}

A | B   #Union of A and B (All elements from both sets. with No Duplicates)
print(A.union(B))
print(A.union(B, C)) #Union of A,B and C

#Intersection

A = {1,2,3,4,5,6,7}
B = {6,7,8,9,10}
print(A & B) #Intersection (common Items) b?w A and B
print(A.intersection(B))  #Intersection of A and B


# Difference
A = {1,2,3,4,5,6,7}
B = {4,5,6,7,8,9,10}
A - B # Set of elements that are only in A but not in B
print(A.difference(B))

print(B.difference(A))  # Set of elements that are only in B but not in A

# Symmetric Difference of sets

A = {1,2,3,4,5,6,7}
B = {4,5,6,7,8,9,10}
A ^ B     #Symmetric Difference of sets
print(A.symmetric_difference(B))

# Subset, superset & Disjoint

A = {1,2,3,4,5,6,7,8,9,10,11}
B = {4,5,6,7,8,9}
C = {10,20,30,40,50}

# This returns Boolean values
print(B.issubset(A))      # Set B is said to be the subset of set A if all elements of B are present
print(A.issubset(B))      # Set A is said to be the superset of set B if all elements of B are present in A

print(C.isdisjoint(A))    # Two sets are said to be disjoint sets if they have no common elements


# Why strings are made immutable in python ?
#Strings are made immutable so that developers cannot alter the contents of object, data security. This avoids unnecessary bug.



var = "This is string data."

# Here , var is an object of type strings.


#immutability
name_1 = 'Rohit'
print(name_1[0])

# Error Message when you want to change the content of the string.
#name_1[0] = 'M'

name_2 = 'M' + name_1[1:]
print("Name1 : " , name_1, " , Name2 : ", name_2)

name_2 = name_1.replace('R','M')
print("Name1 : " , name_1, " , Name2 : ", name_2)


name_1 = 'Rohit'
name_2 = 'Rohit'
print("ID of name_1 : " , id(name_1), " ID of name_2 : ", id(name_2))

# List Methods - append(), extend(), copy(), sort(), remove(), pop()
list_1 = [10, 22+56j, True, False,35, 4000.45, 50.56, True,  False, 12345678, 'This is list']

#pop() removes the element using index position
print(list_1.pop(4))

# Remove() removes the element using value
print(list_1.remove(50.56))

# What is this removing?
print(list_1.remove(0))
print(list_1.remove(1))






      
