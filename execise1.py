def second_largest(numbers):
    largest = None
    second_largest = None

    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
    
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num

    return second_largest

print(second_largest([10, 5, 8, 10, 3]))
print(second_largest([4, 4, 4, 4]))