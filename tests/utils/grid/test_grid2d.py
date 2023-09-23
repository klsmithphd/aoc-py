from utils.grid.grid2d import adj_coords_2d


def test_adj_coords_2d():
    assert {(0, 1), (1, 0), (0, -1), (-1, 0)} == set(adj_coords_2d((0, 0)))
    assert {(-1, 1), (0, 1), (1, 1),
            (-1, 0), (1, 0),
            (-1, -1), (0, -1), (1, -1)} == \
        set(adj_coords_2d((0, 0), diagonals=True))
