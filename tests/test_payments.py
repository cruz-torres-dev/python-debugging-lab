import pytest
from src.fixed.payments import calculate_total

def test_calculate_total_ok():
    assert calculate_total([10, 20, 30]) == 60

def test_calculate_total_empty():
    assert calculate_total([]) == 0

def test_calculate_total_invalid():
    with pytest.raises(Exception):
        calculate_total([10, "x"])

