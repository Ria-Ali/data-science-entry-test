def swap(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    x = x + y
    y = x - y
    x = x - y

    print("Swapped values:", x, y)

swap ("apple", 10)
swap (9, 17)
