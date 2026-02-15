import pytest
from src.fixed.parser import get_user_id

def test_get_user_id_ok():
    assert get_user_id('{"user":{"id":"12"}}') == 12

def test_get_user_id_invalid_json():
    with pytest.raises(Exception):
        get_user_id("{bad json}")

def test_get_user_id_missing_key():
    with pytest.raises(Exception):
        get_user_id('{"foo": 1}')

