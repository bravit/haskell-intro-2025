def process_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:  # Check if the number is odd
            total += num ** 2  # Square it and add to the total
    return total

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_numbers(numbers)

print("Processed result:", result)