from bank import value

def test_hello():
    assert value("hello") == 0

def test_capital():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("Welcome") == 100

def test_h():
    assert value("Hi") == 20
    assert value("hola")== 20

def test_no_h():
    assert value("whats up") == 100
    assert value("welcome") == 100

def test_phrase():
    assert value("hello, welcome to the bank")== 0
    assert value("hi, how can I help you") == 20
    assert value ("welcome to the bank") == 100