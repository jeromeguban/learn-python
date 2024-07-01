# return <expression/value>

def addition(a, b):
    return a + b

add = addition(10, 20)

def demo(a, b):
    return a + b, a - b

print(add)

add, sub = demo(5, 3)
print(add)
print(sub)