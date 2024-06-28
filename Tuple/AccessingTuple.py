

#Difference between lis and tuple
#https://chatgpt.com/share/7fb0c737-566b-409d-b0df-a8976ba9f600

#list

a = [1,2,3]

print(type(a))

#tuple

a = (1,2,3)
print(type(a))

#empty tuple
a = ()
print(type(a))

# tuple with single value
#  read as int
a = (1)
print(type(a)) 

#  read as tuple
a = (1,)
print(type(a)) 

#  without parenthesis
a = 1,2,3,4,5,6
print(type(a)) 

#  list convert to tuple 
l = [1,2,3,4,5]
a = tuple(l)
print(type(l), type(a)) 


#nested tuples
a = (1, (2,3))
print(type(a))

# tuple with mixed datatype
a = (1, "A", 4)
print(a)
print(type(a))

# using index
a = (1,2,3,4,5,6)
print(a)

#using slice Operator
print(a[1:5:1])
print(a[1:5])
print(a[0:3])

