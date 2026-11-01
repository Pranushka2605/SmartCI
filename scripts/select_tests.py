
import argparse
from pathlib import Path

TEST_MAPPING = {
    "src/cart.py": "tests/test_cart.py",
    "src/inventory.py": "tests/test_inventory.py",
    "src/pricing.py": "tests/test_pricing.py",
}

def select_tests(changed_files):
    selected_tests = set()

    for file in changed_files:
        file = file.strip()

        if file in TEST_MAPPING:
            selected_tests.add(TEST_MAPPING[file])

    return sorted(selected_tests)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    changed_files = Path(args.input).read_text(
        encoding="utf-8"
    ).splitlines()

    selected_tests = select_tests(changed_files)

    print("Selected test files:")

    for test in selected_tests:
        print(test)

    Path("selected_tests.txt").write_text(
        "\n".join(selected_tests) + ("\n" if selected_tests else ""),
        encoding="utf-8"
    )
