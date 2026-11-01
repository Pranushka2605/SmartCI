
import subprocess
import sys
from pathlib import Path

TEST_MAPPING = {
    "src/cart.py": "tests/test_cart.py",
    "src/inventory.py": "tests/test_inventory.py",
    "src/pricing.py": "tests/test_pricing.py",
}

def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.splitlines()


def select_tests(changed_files):
    selected_tests = set()

    for file in changed_files:
        if file in TEST_MAPPING:
            selected_tests.add(TEST_MAPPING[file])

    return sorted(selected_tests)


if __name__ == "__main__":
    changed_files = get_changed_files()
    selected_tests = select_tests(changed_files)

    if not selected_tests:
        print("No mapped source changes found.")
        sys.exit(0)

    print("Changed files:")
    for file in changed_files:
        print(file)

    print("\nSelected test files:")
    for test in selected_tests:
        print(test)

    Path("selected_tests.txt").write_text(
        "\n".join(selected_tests) + "\n",
        encoding="utf-8"
    )
