# creating Lists
# Declaring list Object 

a = []
print(a)

a = [1,2,3,4,5,6]
print(a)

# using split() Function

s = ' I love python programming'
a = s.split()
print(a)
print(type(a))


# using List() function

a = list(range(10,20,2))

print(a)


# list of numbers 

a = [1,2,3,4,5]
print(a)

# list of strings

a = ['python', 'programming']
print(a)

# List of mixed datatypes

a = [1, 'a', 2, 'b']

print(a)


# nested List
# a list within the list

a = [1,2,['a','b']]
print(a)
print(a[2])
print(a[2][0])



# Accessing elements of the lists

a = [1,2,3,4,5,6,7,8,9,10]

print(a[0]) # 1
print(a[-1]) # 10


# Slice operator to acess elements ofthe given list
# list-name[start : stop : step]
print(a[1:10:2]) 
print(a[1:10])




