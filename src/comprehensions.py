# this is why we do list comprehensions - it is so much more readable
list_test = [integer for integer in range(10) if integer % 2]
print(list_test)

dict_test = {key: value for key, value in enumerate(list_test)}
print(dict_test)

dict_test = {value: key for key, value in enumerate(list_test)}
print(dict_test)

set_creation = {var for var in list_test}
print(set_creation)
print(type(set_creation))

comp_generator = (var for var in list_test)
for var in comp_generator:
    print(var, end=' ')
print
