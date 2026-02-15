from collections import Counter
from typing import Dict, List

def count_items(items: List[str]) -> Dict[str, int]:
    if not isinstance(items, list):
        raise TypeError("items must be a list")
    return dict(Counter(items))

