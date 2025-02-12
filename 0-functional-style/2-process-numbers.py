def process_numbers(numbers):
    filtered_numbers = []

    # Filter out even numbers
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)

    squared_numbers = []

    # Square the remaining numbers
    for num in filtered_numbers:
        squared_numbers.append(num ** 2)

    # Sum them up
    total = 0
    for num in squared_numbers:
        total += num

    return total

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_numbers(numbers)

print("Processed result:", result)