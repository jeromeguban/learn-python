a = dict({ 1: 'python', 2: 'php', 3: 'java', 4:'ruby'})

for key, value  in a.items(): # return the key value pairs that exst on the dictionary
    print(key,"", value)
    
for i in a:
    print(i, a[i])