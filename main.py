import csv
import os
import json
from pathlib import Path


def main():
    full_base_path = Path(__file__).resolve().parent
    input_filename = full_base_path / "test_scores.csv"

    scores_list = read_csv(input_filename)
    average_final, unique_students = generate_scores(scores_list)

    write_output(average_final, unique_students)


def read_csv(input_filename):
    with open(input_filename) as f:
        scores_list = []
        reader = csv.DictReader(f)
        for row in reader:
            scores_list.append(row)
        return scores_list


def generate_scores(list):
    final_score = 0
    final_num = 0
    student_ids = []
    for row in list:
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
    unique_students = len(student_ids)
    average_final = format_float(average(final_score, unique_students))

    return average_final, unique_students


def average(numerator, denominator):
    try:
        average = numerator/denominator
    except ZeroDivisionError:
        average = 0
    return average



def format_float(float):
    formatted_str = f"{float:.2f}"
    return formatted_str


def write_output(average_final, unique_students):
    output_filename = "output.json"

    if os.path.exists(output_filename):
        os.remove(output_filename)

    result = {
        "average_final": average_final,
        "unique_students": unique_students,
    }

    with open(output_filename, "w") as out:
        json.dump(result, out, indent=2)

if __name__ == "__main__":
    main()
