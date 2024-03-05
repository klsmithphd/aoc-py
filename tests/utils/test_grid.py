import utils.grid as grid


def test_turn():
    assert {'pos': (0, 0), 'heading': 'n'} == \
        grid.turn({'pos': (0, 0), 'heading': 'e'}, 'left')


def test_forward():
    assert {'pos': (5, 1), 'heading': 'e'} == \
        grid.forward({'pos': (-3, 1), 'heading': 'e'}, 8)
