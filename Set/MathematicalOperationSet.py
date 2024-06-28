a = {1,2,3}
b= {3,4,5,6}

# union()
print(a.union(b)) # Join all the values of two set
print(a | b)


# intersection()
print(a.intersection(b)) # get the common value of two set
print(a & b)


# difference()
print(a.difference(b)) # get the element that not exist on the other set
print(b.difference(a))
print( a - b)
print( b - a)


# symetric_difference()
print(a.symmetric_difference(b)) # exclude the element that has same value & combile all elements to one set
print(a ^ b)


