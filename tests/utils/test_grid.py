import utils.grid as grid


def test_turn():
    assert {'pos': (0, 0), 'heading': 'n'} == \
        grid.turn({'pos': (0, 0), 'heading': 'e'}, 'left')


def test_forward():
    assert {'pos': (5, 1), 'heading': 'e'} == \
        grid.forward({'pos': (-3, 1), 'heading': 'e'}, 8)


def test_interpolated():
    assert [(1, 4), (2, 4), (3, 4), (4, 4)] == \
        grid.interpolated((1, 4), (4, 4))
    assert [(3, 2), (3, 1), (3, 0), (3, -1)] == \
        grid.interpolated((3, 2), (3, -1))
    assert [(1, 1)] == grid.interpolated((1, 1), (1, 1))
