a = 10
b = 20
c = 30
d = 40

#packing
e = a,b,c,d
print(e)

#unpacking
# reminder when unpacking a tuple the variable must be the same count
w, x, y, z = e

print(w) #10
print(x) #20
print(y) #30
print(z) #50