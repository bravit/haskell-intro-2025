def process_numbers(numbers):
    return \
        sum(
            map(lambda x: x**2,
                filter(lambda x: x % 2 != 0, numbers)))

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_numbers(numbers)

print("Processed result:", result)