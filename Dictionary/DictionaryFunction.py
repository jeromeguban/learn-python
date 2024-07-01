
a = dict({ 1: 'python', 2: 'php', 3: 'java', 4:'ruby'})

# len() count the length of dictionary values

print(len(a))

# get(key, default_value) used to get correspnding value of key pair

print(a.get(1))
print(a.get(2))
print(a.get(1,100))
# keys() get all the keys on the dictionary
print(a.keys())
print(type(a.keys()))
print(list(a.keys()))
# values  get all the values on the dictionary
print(a.values())
print(type(a.values()))
print(list(a.values()))
# items() return the key value pair of the given dictionary
print(a.items())
print(type(a.items()))
print(list(a.items()))