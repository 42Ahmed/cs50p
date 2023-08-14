from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(11)