from twttr import shorten


def test_twitter():
    assert shorten("twitter") == "twttr"
    assert shorten("Ahmed") == "hmd"


def test_constant():
    assert shorten("ty") == "ty"
    assert shorten("hll") == "hll"


def test_vowel():
    assert shorten("aeiou") == ""
    assert shorten("ea") == ""


def test_not_alpha():
    assert shorten("$10.00") == "$10.00"


def test_capital():
    assert shorten("HELLO") == "HLL"
