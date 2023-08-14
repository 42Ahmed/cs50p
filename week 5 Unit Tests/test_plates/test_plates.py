from plates import is_valid


def test_length():
    assert is_valid("a") == False
    assert is_valid("aaaaaa123") == False
    assert is_valid("aa123") == True


def test_two_chars():
    assert is_valid("aa") == True
    assert is_valid("a1") == False
    assert is_valid("a123") == False


def test_invalid_char():
    assert is_valid("aa3!") == False
    assert is_valid("aa 3") == False
    assert is_valid("aa3.0") == False


def test_num_then_al():
    assert is_valid("aa3a") == False
    assert is_valid("hi23f") == False
    assert is_valid("hi23") == True


def test_start_with_zero():
    assert is_valid("aa03") == False
    assert is_valid("aa30") == True
