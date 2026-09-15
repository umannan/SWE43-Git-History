def calculate_average(grades):
    if not grades:
        return 0

    for grade in grades:
        if grade < 0 or grade > 100:
            raise ValueError("Grades must be between 0 and 100.")

    total = sum(grades)
    return total / len(grades)


grades = [85, 90, 78, 92]
average = calculate_average(grades)

print("Grades:", grades)
print("Average:", average)