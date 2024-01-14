import utils.core as u


def test_index_of():
    assert 3 == u.index_of(lambda x: x == 8, [1, 2, 4, 8, 16])
    assert 0 == u.index_of(lambda x: x == 2, [2, 2, 2, 2, 2, 2])
    assert None == u.index_of(lambda x: x == 8, [1, 3, 9, 27, 81])
