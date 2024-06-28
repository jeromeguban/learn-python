a = {1,2,3,4,5}

# add()
a.add(6)
print(a)

#adding multiple
# a.add(10,20,30)  # Error
# print(a)

a.update([7,8,9,10])
print(a)

#update() with range()
a.update(a, range(20))
print(a)


#copy()
b = a.copy()
print(a)