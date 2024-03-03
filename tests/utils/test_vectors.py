import utils.core as u
import utils.vectors as v


def test_scalar_mul():
    # If the input vec is represented as a tuple, a tuple is returned
    assert (5, 10, 15) == v.scalar_mul((1, 2, 3), 5)
    # If the input vec is represented as a list, a list is returned
    assert [5, 10, 15] == v.scalar_mul([1, 2, 3], 5)
    # The vectors can be any dimension (length)
    assert [0, 0, 0, 0] == v.scalar_mul([1, 2, 3, 4], 0)
    assert [1.0, 2.0, 3.0] == v.scalar_mul([2, 4, 6], 0.5)
    # If the input vec is an iterator, an iterator is returned
    assert u.iter_equals(iter([6, 2, 4]),
                         v.scalar_mul(iter([3, 1, 2]), 2))


def test_vec_sum():
    # If the first vector is a tuple, a tuple is returned
    assert (1, 2, 3) == v.vec_sum([(0, 0, 0), (1, 2, 3)])
    # If the first vector is a list, a list is returned
    assert [1, 2, 3] == v.vec_sum([[1, 2, 3]])
    # The function can accept a collection of any number of vectors
    assert [12, 15, 18] == v.vec_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # If the first vector is an iterator, an iterator is returned
    assert u.iter_equals(iter([1, 2, 3]),
                         v.vec_sum([iter([1, 2, 3])]))


def test_vec_add():
    assert (6, 8) == v.vec_add((2, 10), (4, -2))
    assert [6, 8] == v.vec_add([2, 10], [4, -2])
