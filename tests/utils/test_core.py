import collections as c
import utils.core as u


Point = c.namedtuple("Point", ["x", "y"], defaults=[0]*2)


def test_index_of():
    assert 3 == u.index_of(lambda x: x == 8, [1, 2, 4, 8, 16])
    assert 0 == u.index_of(lambda x: x == 2, [2, 2, 2, 2, 2, 2])
    assert None == u.index_of(lambda x: x == 8, [1, 3, 9, 27, 81])


def test_nt_set():
    assert Point(3, 2) == u.nt_set(Point(), {"x": 3, "y": 2})


def test_nt_update():
    assert Point(3, -2) == u.nt_update(Point(), {"x": u.add(3),
                                                 "y": u.add(-2)})


def test_without_keys():
    assert {"x": 1, "y": 2} == \
        u.without_keys({"x": 1, "y": 2, "z": 3}, ["z", "a"])


def test_product():
    assert 6 == u.product([1, 2, 3])
    assert 10 == u.product([10])
    assert 1 == u.product([])


def test_rotate():
    assert [0, 1, 2, 3, 4] == list(u.rotate(0, range(5)))

    assert [1, 2, 3, 4, 0] == list(u.rotate(1, range(5)))
    assert [2, 3, 4, 0, 1] == list(u.rotate(2, range(5)))
    assert [3, 4, 0, 1, 2] == list(u.rotate(3, range(5)))
    assert [4, 0, 1, 2, 3] == list(u.rotate(4, range(5)))
    assert [0, 1, 2, 3, 4] == list(u.rotate(5, range(5)))

    assert [4, 0, 1, 2, 3] == list(u.rotate(-1, range(5)))
    assert [3, 4, 0, 1, 2] == list(u.rotate(-2, range(5)))
    assert [2, 3, 4, 0, 1] == list(u.rotate(-3, range(5)))
    assert [1, 2, 3, 4, 0] == list(u.rotate(-4, range(5)))
    assert [0, 1, 2, 3, 4] == list(u.rotate(-5, range(5)))
