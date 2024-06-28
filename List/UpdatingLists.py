a = [1,2,3,4,5,6,7,8,9,10,11]

# add new elements
# using index to change the value
a[10] = 100
print(a)

a[1:4] = [33,34,35]
print(a)

#Using Slicing operator to change value
a[1:4] = [32,33,34] #change the value of 2,3 and 4
print(a)

#using append function

a.append(200)
a.append(300)
print(a)

# using extend function
# used to append a list to an existing list
a.extend([400,500,600])
print(a)

# using insert() function
#index, new value
a.insert(1,100)
print(a)




# delete elements
# del function
del a[1]
print(a)
# del function using range
del a[1:3]
print(a)

#remove() function
a.remove(600) 
print(a)

#pop() function

a.pop()
print(a)

#clear() function

a.clear()
print(a)

a.append(1)
print(a)


