from src.fixed.inventory import count_items

def test_count_items_ok():
    assert count_items(["a", "b", "a"]) == {"a": 2, "b": 1}

def test_count_items_empty():
    assert count_items([]) == {}

