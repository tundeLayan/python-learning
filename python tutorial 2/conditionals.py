user = 'Admin'
logged_in = False

# if user == 'Admin' and logged_in == True:
#   print('Logged in')

a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))

# is checks the location similar to id(a) == id(b)
print(a is b)

print(a == b)