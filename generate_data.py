import csv
import random

random.seed(42)

# Generate 300 build records
n = 300

with open("ml_builds.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "files_changed",
        "lines_changed",
        "tests_touched",
        "hour",
        "failed"
    ])

    for i in range(n):
        files_changed = random.randint(1, 19)
        lines_changed = random.randint(10, 999)
        tests_touched = random.randint(0, 14)
        hour = random.randint(0, 23)

        risk = (
            0.10
            + files_changed * 0.015
            + lines_changed * 0.0002
            - tests_touched * 0.015
            + (0.10 if hour >= 22 else 0)
        )

        risk = max(0.05, min(0.90, risk))
        failed = 1 if random.random() < risk else 0

        writer.writerow([
            files_changed,
            lines_changed,
            tests_touched,
            hour,
            failed
        ])

print("Dataset generated successfully!")
print("Total records:", n)