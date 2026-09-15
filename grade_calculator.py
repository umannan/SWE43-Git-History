def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)


grades = [85, 90, 78, 92]
average = calculate_average(grades)

print("Grades:", grades)
print("Average:", average)