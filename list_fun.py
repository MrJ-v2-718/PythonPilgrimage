# MrJ
# 8/30/2023
# Purpose: Calc grades using lists

# Variables
midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

all_scores = midterm_scores + final_scores

# Get length of lists & print
num_mid_scores = len(midterm_scores)
num_final_scores = len(final_scores)
print(num_mid_scores, "students took the midterm.")
print(num_final_scores, "students took the final.")

# Calc amount of dropped students
dropped_students = num_mid_scores - num_final_scores
print(dropped_students, "students must have dropped the class.")

# Calc & print range of scores
low_final = min(final_scores)
highest_final = max(final_scores)
print(f"\nFinal scores ranged from {low_final} to {highest_final}")

# Calculate the average midterm and final
avg_midterm = sum(midterm_scores) / num_mid_scores
final_scores = sum(final_scores) / num_final_scores
print(f"The average midterm score was {avg_midterm:.2f}")
print(f"The average midterm score was {avg_midterm:.2f}")
