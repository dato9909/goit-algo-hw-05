from typing import Callable
import re

text = "Зарплата працівника складається з основної виплати в розмірі 2000 доларів на місяць, а також додаткових бонусів у розмірі 500 доларів і 150 доларів."

def generator_numbers(text: str):
    pattern = r"\d+\.\d+|\d+"

    find_numbers = re.findall(pattern, text)

    for number in find_numbers:
        yield float(number)

def sum_profit(text: str, gen_func: Callable):

    gen = gen_func(text)

    total = sum(gen)

    return total

total_income = sum_profit(text,generator_numbers)
print(f"Загальний дохід: {total_income}")
