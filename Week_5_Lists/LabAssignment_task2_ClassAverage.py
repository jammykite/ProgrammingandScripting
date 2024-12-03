"""
Write a program that:
1. Accepts grades from the user (use a loop).
2. Stores the grades in a list.
3. Calculates and prints the average grade.
"""

def get_grades():
    """Accept grades from the user and store them in a list."""
    grades = []
    while True:
        grade_input = input("Enter a grade (or type 'done' to finish): ").strip()
        if grade_input.lower() == 'done':
            break
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return grades

def calculate_average(grades):
    """Calculate and return the average of the grades."""
    if grades:
        return sum(grades) / len(grades)
    return 0

def classaverage():
    """Main function to accept grades, calculate, and print the average."""
    print("Grade Entry Program")
    grades = get_grades()
    if grades:
        average = calculate_average(grades)
        print(f"\nGrades entered: {grades}")
        print(f"Average grade: {average:.2f}")
    else:
        print("\nNo grades were entered.")

# Run the program
if __name__ == '__main__':
    classaverage()
