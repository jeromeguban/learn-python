a = (1,2,3,4,5,6,7,8,9,10,11)

# a[0] = 100 #Error: 'tuple' object does not support item assignment

a = (1,2,3,[4,5,6]) # can used item assignment if you have list inside the tuple

a[3][0] = 10

print(a)


