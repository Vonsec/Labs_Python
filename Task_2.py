# TODO импортировать необходимые молули
import csv
import json
from itertools import islice
from pathlib import Path
from typing import Iterator, Dict


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def read_csv(file_path: str, delimiter: str = ",") -> Iterator[Dict[str, str]]:
    with file_path.open(mode='r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in reader:
            yield row


def task() -> None:
    ...  # TODO считать содержимое csv файла
    input_path = Path(INPUT_FILENAME)
    output_path = Path(OUTPUT_FILENAME)
    data_generator = read_csv(input_path, delimiter=",")
    data = list(islice(data_generator, None))

    ...  # TODO Сериализовать в файл с отступами равными 4
    with output_path.open(mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    output_path = Path(OUTPUT_FILENAME)
    with output_path.open(mode='r', encoding='utf-8') as output_f:
        content = output_f.read()
        print(content.rstrip('\n'), end='')
