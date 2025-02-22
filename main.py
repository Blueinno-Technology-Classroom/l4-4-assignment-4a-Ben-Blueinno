# ✅ Complete this function, replace `pass` with your solution:
def find_min_max(numbers) -> dict:
    ############ method 2 ############
    # min = numbers[0]
    # for num in numbers:
    #     if num < min:
    #         min = num
    # max = numbers[0]
    # for num in numbers:
    #     if num > max:
    #         max = num
    ############ method 2 ############
    mymin = min(numbers)
    mymax = max(numbers)
    return {'min': mymin, 'max': mymax}


############### ❌ DO NOT change these lines ###############
list1 = [1, 2, 3, 2, -1, 5]
list2 = [21, 2.5, -3, -2, -1, 5.1]

result1 = find_min_max(list1)
result2 = find_min_max(list2)

print(result1)  # --> {'min': -1, 'max': 5}
print(result2)  # --> {'min': -3, 'max': 21}
############### ❌ DO NOT change these lines ###############
