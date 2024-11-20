# TODO решите задачу
import json


def task() -> float:
    with open("input.json", 'r') as f:
        data = json.load(f)
    return sum([i["score"] * i["weight"] for i in data])


print(f'{task():.3f}')
