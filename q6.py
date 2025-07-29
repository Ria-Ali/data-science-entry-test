def find_first_negative(l\lst):
    i = 0 
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]  
        i += 1 
    return 

print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))


# i didn't know how to do this at all. Had to use CoPilot. Gemini generated a different answer;

def find_first_negative_loop(numbers):
    for num in numbers:
        if num < 0:
            return num
    return None  # Return None if no negative number is found


def find_first_negative_next(numbers):
    return next((num for num in numbers if num < 0), None)

# looks easier - but i still don't get it. 
