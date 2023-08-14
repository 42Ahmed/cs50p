from fuel import convert, gauge
import pytest

def test_percent():
    assert convert("1/4") == 25
    assert convert("1/2") == 50

def test_errors():
    with pytest.raises(ZeroDivisionError):
         convert('2/0')
    with pytest.raises(ValueError):
         convert('3/2')

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"