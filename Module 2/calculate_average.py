import pdb

def calculate_average(numbers):
    pdb.set_trace()  # <-- Breakpoint
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

grades = [90, 85, 78]
average = calculate_average(grades)
print("Average grade:", average)

