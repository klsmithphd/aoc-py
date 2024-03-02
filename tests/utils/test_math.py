import utils.math as math


def test_mod_pow():
    assert 1 == math.mod_pow(15, 2, 0)
    assert 8 == math.mod_pow(10, 2, 3)
    assert 2 == math.mod_pow(3, 2, 5)
