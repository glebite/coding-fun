list_test = [i for i in range(10) if i % 2]
print(list_test)

dict_test = {key: value for key, value in enumerate(list_test)}
print(dict_test)

dict_test = {value: key for key, value in enumerate(list_test)}
print(dict_test)
