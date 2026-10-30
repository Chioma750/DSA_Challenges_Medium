def second_largest(numbers):
    largest = numbers[0]
    second_largest = numbers[0]

    if second_largest == []:
        return None

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
    
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

print(second_largest([10, 5, 8, 10, 3]))
print(second_largest([4, 4, 4, 4]))