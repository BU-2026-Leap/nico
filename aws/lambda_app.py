from aws.s3_data_fetcher import S3DataFetcher
from common.exam_data_processor import ExamDataProcessor
from common.contracts import read_and_compute

import base64
import os

def build_html(stats):
  img_path = os.path.join(os.environ['LAMBDA_TASK_ROOT'],"common/funnydog.png")

  with open(img_path, "rb") as f:
    data= base64.b64encode(f.read()).decode("utf-8")

    return f"""<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Summary of All</title>
    <style>
      h1 {{
        font-family: georgia;
      }}
      table {{
        border-collapse: collapse;
        width: 80%
      }}
      td, th {{
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      }}
    </style>
  </head>
  <body>
    <img src="data:image/png;base64,{data}" alt="silly dog">
    <h1>Hiiiiiiiiiiiiiiiiiiii</h1>
    <h1>Student Scores!</h1>
    <table>
      <tr>
        <th><strong>Average score:</strong></th>
        <th><strong>Unique students:</strong></th>
      </tr>
      <tr>
        <td>{stats.average_final}</td>
        <td>{stats.unique_students}</td>
      </tr>
    </table>
  </body>
</html>
"""

def lambda_handler(event, context):
    print("Starting lambda!")

    result = read_and_compute(
        S3DataFetcher("bulead2026-exam-scores", "test_scores.csv"),
        ExamDataProcessor()
    )

    print(result)

    return {
        'statusCode': 200,
        'headers': {"Content-Type": "text/html; charset=utf-8"},
        'body': build_html(result)
    }