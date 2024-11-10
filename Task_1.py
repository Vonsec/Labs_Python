import json
import operator
from typing import List, Dict


# TODO решите задачу
def task() -> float:
    filename = 'input.json'

    with open(filename, 'r', encoding='utf-8') as file:
        data: List[Dict[str, float]] = json.load(file)

    products = map(operator.mul,
                   (item["score"] for item in data),
                   (item["weight"] for item in data))

    total = sum(products)
    return round(total, 3)


print(task())
