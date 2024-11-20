# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as f:
        reader = csv.DictReader(f)

        json_data = []

        for row in reader:
            tmp = {
                'longitude': row['longitude'],
                'latitude': row['latitude'],
                'housing_median_age': row['housing_median_age'],
                'total_rooms': row['total_rooms'],
                'total_bedrooms': row['total_bedrooms'],
                'population': row['population'],
                'households': row['households'],
                'median_income': row['median_income'],
                'median_house_value': row['median_house_value'],

            }
            json_data.append(tmp)

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(json_data, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
