def update_dictionary(dct, key, value):
    if not isinstance(dct, dict):
        return -1  

    if key in dct:
        print("Original value for key '{}' was: {}".format(key, dct[key]))

    dct[key] = value  
    return dct

result1 = update_dictionary({}, "name", "Alice")
print(result1)

result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
