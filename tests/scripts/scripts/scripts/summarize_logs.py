import argparse
import re
from pathlib import Path


def summarize_logs(log_file):
    path = Path(log_file)

    if not path.exists():
        print("Error: Log file not found.")
        return

    content = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    patterns = re.compile(
        r"ERROR|FAILED|Traceback|Exception|"
        r"AssertionError|BUILD FAILED",
        re.IGNORECASE
    )

    errors = [
        line for line in content.splitlines()
        if patterns.search(line)
    ]

    prompt = "LLM-Based Build/Error-Log Analysis\n\n"

    if errors:
        prompt += "Detected errors:\n"
        for error in errors:
            prompt += f"- {error}\n"
    else:
        prompt += "No common error patterns were detected.\n"

    prompt += (
        "\nPlease explain the errors, identify their "
        "possible causes, and suggest solutions."
    )

    Path("llm_prompt.txt").write_text(
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
    