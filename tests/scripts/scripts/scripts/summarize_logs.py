from pathlib import Path
import re
import argparse


def extract_errors(log_text):
    patterns = [
        r"ERROR",
        r"FAILED",
        r"Traceback",
        r"Exception",
        r"AssertionError",
        r"ModuleNotFoundError",
        r"ImportError",
    ]

    errors = []

    for line in log_text.splitlines():
        if any(re.search(pattern, line, re.IGNORECASE)
               for pattern in patterns):
            errors.append(line)

    return errors


def summarize_logs(log_file):
    path = Path(log_file)

    if not path.exists():
        print("Error: Log file not found.")
        return

    content = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    errors = extract_errors(content)

    if errors:
        summary = "LLM Log Summary\n\n"
        summary += "Errors found in the build log:\n\n"
        summary += "\n".join(errors)
    else:
        summary = "LLM Log Summary\n\n"
        summary += "No errors found in the build log."

    Path("llm_prompt.txt").write_text(
        summary,
        encoding="utf-8"
    )

    print(summary)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Summarize CI build logs"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the build log file"
    )

    args = parser.parse_args()

    summarize_logs(args.input)