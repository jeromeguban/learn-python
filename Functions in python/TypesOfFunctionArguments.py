
# required arguments - arguments that are required to be passed in a function

def print_hello(name):
    print("Hello", name)


# keyword arguments - You can define argument name by calling the function

def user_info(name, age):
    print("Hello!", name, "Your age is :", age)

# default arguments

def user_info_default( name = "Gab", age = 27):
    print("Hello!", name, "Your age is :", age)

#variable length arguments

def greet(*name):
    for s in name: 
        print("Hello!", s)


print_hello("Edward")

user_info("Edward", 26)
user_info(name="Edward", age=26)


user_info_default()

user_info_default('Edward', 26)


greet("Gab", "Edward", 'Raymart', "Brynd")
