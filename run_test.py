import json
from cortexone_function import run

def main():
    with open("tests/test_inputs.json", "r", encoding="utf-8") as f:
        input_data = json.load(f)

    result = run(input_data)
    print(json.dumps(result, indent = 2))

if __name__ == "__main__":
    main()