import json
import os
import subprocess
import sys
from pathlib import Path
from main import average, format_float, generate_scores, write_output

def test_average():
    nominators = [0, 1, 5, 100, 1000]
    denominators = [0, 1, 5, 100, 1000]
    for nom in nominators:
        for denom in denominators:
            result = average(nom, denom)
            if denom == 0 or nom == 0:
                assert result == 0
            elif denom == 1:
                assert result == nom
            elif denom == nom:
                assert result == 1

def test_format_float():
    result_up = format_float(2.99999)
    assert result_up == '3.00'

    result_down = format_float(2.111111)
    assert result_down == '2.11'



def test_script_output():
    repo_root = Path(__file__).resolve().parents[0]
    print("repo: " + str(repo_root))
    output_filename = "output.json"

    result = subprocess.run(
        [sys.executable, "-m", "main"],
        cwd=str(repo_root),
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, (
        f"Return code: {result.returncode}\n"
        f"cwd used: {repo_root}\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}\n"
    )

    assert os.path.exists(output_filename)

    with open(output_filename) as f:
        main_output = json.load(f)

        # Make sure only two items in dict
        assert len(main_output) == 2

        # Check for correct avg
        assert "average_final" in main_output
        assert main_output["average_final"] == '87.33'

        # Check for correct number of students
        assert "unique_students" in main_output
        assert main_output["unique_students"] == 3

