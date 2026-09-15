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

def print_student_summary(student_name, grades, weights):
    average = calculate_weighted_average(grades, weights)
    letter_grade = get_letter_grade(average)

    print("Student:", student_name)
    print("Grades:", grades)
    print("Weighted Average:", round(average, 2))
    print("Letter Grade:", letter_grade)

def print_all_student_summaries(students, weights):
    if not students:
        print("No student records available.")
        return

    for student in students:
        print_student_summary(student["name"], student["grades"], weights)
        print()

students = []

weights = [0.20, 0.30, 0.20, 0.30]

print_all_student_summaries(students, weights)