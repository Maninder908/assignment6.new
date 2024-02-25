def remove_odd_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_numbers = remove_odd_numbers(numbers)

print("Original list:", numbers)
print("Cut-down list (without odd numbers):", cut_down_numbers)