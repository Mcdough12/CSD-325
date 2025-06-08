def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

grades = [90, 85, 78]
average = calculate_average(grades)
print("Average grade:", average)
