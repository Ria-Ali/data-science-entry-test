def find_and_replace(lst, find_val, replace_val):
    if not isinstance(lst, list):
        return -1
        
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst

result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)

result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)
