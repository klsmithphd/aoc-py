from utils.graph import DictGraph, dijkstra

g1 = DictGraph({'a': {'b': 1},
                'b': {'a': 1, 'c': 2},
                'c': {'b': 2, 'd': 3},
                'd': {'c': 3, 'e': 1},
                'e': {'d': 1}})

g2 = DictGraph({'a': {'b': 1},
                'b': {'a': 1, 'c': 2, 'f': 4},
                'c': {'b': 2, 'd': 3},
                'd': {'c': 3, 'e': 1},
                'e': {'d': 1},
                'f': {'b': 4, 'g': 1},
                'g': {'f': 1}})

g3 = DictGraph({'a': {'b': 7, 'c': 14, 'd': 9},
                'b': {'a': 7, 'd': 10, 'e': 15},
                'c': {'a': 14, 'd': 2, 'f': 9},
                'd': {'a': 9, 'b': 10, 'c': 2, 'e': 11},
                'e': {'b': 15, 'd': 11, 'f': 6},
                'f': {'c': 9, 'e': 6}})


def test_vertices():
    assert {'a', 'b', 'c', 'd', 'e'} == set(g1.vertices())


def test_edges():
    assert {'b'} == set(g1.edges('a'))
    assert {'b', 'd'} == set(g1.edges('c'))


def test_distance():
    assert 2 == g1.distance('b', 'c')
    assert 3 == g1.distance('d', 'c')


def test_dijkstra():
    assert None == dijkstra(g3, 'a', lambda v: v == 'NotANode')
    assert ('a',) == dijkstra(g3, 'a', lambda v: v == 'a')
    assert ('a', 'd', 'e') == dijkstra(g3, 'a', lambda v: v == 'e')
    assert ('a', 'd', 'c', 'f') == dijkstra(g3, 'a', lambda v: v == 'f')
