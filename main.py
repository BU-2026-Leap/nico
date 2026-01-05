import csv
import os
import json

input_filename = "test_scores.csv"
output_filename = "output.json"

if os.path.exists(output_filename):
    os.remove(output_filename)

average_final = 0.0
unique_students = 0

with open(input_filename) as f:
    reader = csv.DictReader(f)
    final_score = 0
    final_num = 0
    student_ids = []
    for row in reader:
        print(row)
        # Add all final scores
        if row['exam_name'] == 'final':
            final_score += float(row['score'])
            final_num += 1
        else:
            continue

        # Check for unique student ID
        if row['student_id'] not in student_ids:
            student_ids.append(row['student_id'])
    # Find average
    average_final = final_score / final_num
    unique_students = len(student_ids)

    # Print
    print(f"Number of students: {unique_students}")
    print(f"Average final: {average_final:.2f}")

if os.path.exists(output_filename):
    os.remove(output_filename)

result = {
    "average_final": average_final,
    "unique_students": unique_students,
}

with open(output_filename, "w") as out:
    json.dump(result, out, indent=2)

