import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        json_data = [OrderedDict(row) for row in reader]
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Нужно для проверки

    task()
    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
