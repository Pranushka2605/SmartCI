import argparse
from pathlib import Path


def summarize_logs(input_file):
    log_path = Path(input_file)

    if not log_path.exists():
        log_content = "No build log available."
    else:
        log_content = log_path.read_text(
            encoding="utf-8",
            errors="replace"
        )

    prompt = f"""
You are an expert software testing assistant.

Analyze the following CI build log.

Your tasks:
1. Identify whether the tests passed or failed.
2. Identify the errors and exceptions.
3. Explain the possible reasons for failures.
4. Suggest solutions to fix the errors.
5. Provide a short summary of the build result.

CI Build Log:
{log_content}
"""

    Path("llm_prompt.txt").write_text(
        prompt,
        encoding="utf-8"
    )

    print("LLM prompt generated successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate an LLM prompt from CI logs"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the build log"
    )

    args = parser.parse_args()
    summarize_logs(args.input)