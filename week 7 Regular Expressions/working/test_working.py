import pytest
from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    assert convert("9:36 AM to 5:59 PM") == "09:36 to 17:59"

def test_errors():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("9:65 AM to 5:65 PM")
