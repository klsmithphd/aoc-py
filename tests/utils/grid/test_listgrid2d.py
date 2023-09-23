from utils.grid.listgrid2d import ListGrid2D, strings_to_ListGrid

sample = ListGrid2D([[1, 2, 3],
                     [4, 5, 6]])


def test_ListGrid():
    assert 3 == sample.width()
    assert 2 == sample.height()
    assert False == sample.contains((-1, -1))
    assert {(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)} == \
        set(sample.positions())

    assert 5 == sample.value((1, 1))

    assert {(1, 0): 2, (0, 1): 4} == sample.neighbors4((0, 0))
    assert {(0, 1): 4, (1, 0): 2, (2, 1): 6} == sample.neighbors4((1, 1))

    assert {(1, 0): 2, (2, 0): 3, (1, 1): 5} == sample.neighbors8((2, 1))
    assert {(0, 0): 1, (1, 0): 2, (2, 0): 3, (0, 1): 4, (2, 1): 6} == \
        sample.neighbors8((1, 1))


def test_strings_to_ListGrid():
    assert ListGrid2D([[0, 0, 1], [0, 1, 0]]) == \
        strings_to_ListGrid(lambda c: 0 if c == '.' else 1, ["..#", ".#."])
