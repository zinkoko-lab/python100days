# count_lines.py
import subprocess
from pathlib import Path

py_files = subprocess.check_output(["git", "ls-files", "*.py"]).decode().splitlines()
total = 0

for file in py_files:
    path = Path(file)
    if path.exists():
        total += sum(1 for _ in path.open())

print(f"Total lines: {total}")
