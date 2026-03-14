import json
import os
from cortexone_function import run

TEST_DIR = "tests"

def run_test_file(path):
    with open(path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    result = run(input_data)

    print(f"\n===== Test: {os.path.basename(path)} =====")
    print(json.dumps(result, indent=2))


def main():
    for file in os.listdir(TEST_DIR):
        if file.endswith(".json"):
            print(os.path.join(TEST_DIR, file))
            run_test_file(os.path.join(TEST_DIR, file))


if __name__ == "__main__":
    main()