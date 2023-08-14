from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("123.122.122.122") == True
    assert validate("12.88.77.99") == True
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("256.300.270.240") == False
    assert validate("250.230.230.1000") == False
    assert validate("20.10.30.30.30") == False
    assert validate("20,10,30,30") == False
    assert validate("20.10.10") == False
    assert validate("hi") == False
    assert validate("") == False
    assert validate("256.1.1.1") == False
    assert validate("192.300.100.200") == False
    assert validate("192.168.300.200") == False
    assert validate("192.168.1000.200") == False
    assert validate("192.168.100.1000") == False