from typing import Iterable, Union

Number = Union[int, float]

def calculate_total(values: Iterable[Number]) -> Number:
    total: Number = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError(f"Invalid item type: {type(v)}")
        total += v
    return total

