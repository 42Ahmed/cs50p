from um import count

def test_count():
    assert count("") == 0
    assert count("um") == 1
    assert count ("um,yummy") == 1
    assert count("yummy") == 0
    assert count("testing um in sentence") == 1
    assert count("..um,,um??") == 2
    assert count("UM") == 1