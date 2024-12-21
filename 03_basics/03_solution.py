def calculate_grade(assignments, tests, lab_work):
    """
    Calculate the grade of a student based on scores from assignments, tests, and lab work.
    """
    # Calculate the weighted average
    final_score = (0.1 * assignments) + (0.7 * tests) + (0.2 * lab_work)
    
    # Determine the grade based on the final score
    if final_score >= 90:
        grade = "A"
    elif final_score >= 80:
        grade = "B"
    elif final_score >= 70:
        grade = "C"
    elif final_score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return final_score, grade


# Input scores
assignments = float(input("Enter the score for Assignments (out of 100): "))
tests = float(input("Enter the score for Tests (out of 100): "))
lab_work = float(input("Enter the score for Lab Work (out of 100): "))

# Calculate the final score and grade
final_score, grade = calculate_grade(assignments, tests, lab_work)

# Display the results
print("\n----- Grade Report -----")
print(f"Final Score: {final_score:.2f}")
print(f"Grade: {grade}")
