def calculate_average(grades):
    if not grades:
        return 0

    for grade in grades:
        if grade < 0 or grade > 100:
            raise ValueError("Grades must be between 0 and 100.")

    total = sum(grades)
    return total / len(grades)


def get_letter_grade(average):
    if average > 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


grades = [90, 90, 90, 90]
average = calculate_average(grades)
letter_grade = get_letter_grade(average)

print("Grades:", grades)
print("Average:", average)
print("Letter Grade:", letter_grade)