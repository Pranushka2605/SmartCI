
import argparse
from pathlib import Path

TEST_MAPPING = {
    "src/cart.py": "tests/test_cart.py",
    "src/inventory.py": "tests/test_inventory.py",
    "src/pricing.py": "tests/test_pricing.py",
}

def get_changed_files(input_file):
    path = Path(input_file)

    if not path.exists():
        print(f"Error: {input_file} not found.")
        return []

    return path.read_text(encoding="utf-8").splitlines()


def select_tests(changed_files):
    selected_tests = set()

    for file in changed_files:
        file = file.strip().replace("\\", "/")

        if file in TEST_MAPPING:
            selected_tests.add(TEST_MAPPING[file])

    return sorted(selected_tests)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="changed_files.txt")
    args = parser.parse_args()

    changed_files = get_changed_files(args.input)
    selected_tests = select_tests(changed_files)

    print("Changed files:")
    for file in changed_files:
        print(file)

    if not selected_tests:
        print("No mapped source changes found.")
    else:
        print("\nSelected test files:")
        for test in selected_tests:
            print(test)

    Path("selected_tests.txt").write_text(
        "\n".join(selected_tests) + ("\n" if selected_tests else ""),
        encoding="utf-8"
    )
