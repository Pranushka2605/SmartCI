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
        r"ImportError"
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

    log_text = path.read_text(
        encoding="utf-8",
        errors="replace"
    )

    errors = extract_errors(log_text)

    if errors:
        result = "\n".join(errors[-30:])

        prompt = f"""
You are a CI/CD debugging assistant.

Analyze the following build error logs.

1. Identify the main error.
2. Explain the likely cause.
3. Identify the affected test or file.
4. Suggest a possible solution.

Explain in simple language.

ERROR LOGS:
{result}
"""
    else:
        prompt = """
No common error patterns were detected
in the captured logs.

Check the complete build log to confirm
whether the build was successful.
"""

    output_file = Path("llm_prompt.txt")

    output_file.write_text(
        prompt,
        encoding="utf-8"
    )

    print("Log analysis preparation completed.")
    print("LLM prompt saved in llm_prompt.txt")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="build.log"
    )

    args = parser.parse_args()

    summarize_logs(args.input)