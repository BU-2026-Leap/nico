import json
import os
import subprocess
import sys
from pathlib import Path

def test_script_output():
    repo_root = Path(__file__).resolve().parents[1]
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