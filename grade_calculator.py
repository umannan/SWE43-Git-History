def validate_grades(grades):
    if not grades:
        raise ValueError("At least one grade is required.")

    for grade in grades:
        if grade < 0 or grade > 100:
            raise ValueError(f"Invalid grade {grade}: grades must be between 0 and 100.")


def calculate_average(grades):
    validate_grades(grades)
    return sum(grades) / len(grades)


def validate_weights(grades, weights):
    if len(grades) != len(weights):
        raise ValueError("Each grade must have a corresponding weight.")

    if abs(sum(weights) - 1.0) > 0.001:
        raise ValueError(
    f"Invalid weights: weights must add up to 1.0, but total {sum(weights):.2f}."
)


def calculate_weighted_average(grades, weights):
    validate_grades(grades)
    validate_weights(grades, weights)

    return sum(grade * weight for grade, weight in zip(grades, weights))

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


grades = [85, 90, 78, 92]
weights = [0.20, 0.30, 0.20, 0.30]

average = calculate_weighted_average(grades, weights)
letter_grade = get_letter_grade(average)

print("Grades:", grades)
print("Weighted Average:", average)
print("Letter Grade:", letter_grade)