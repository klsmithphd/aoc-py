from utils.graph import DictGraph, astar, dijkstra

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

# g4 graph and g4_heur from https://en.wikipedia.org/wiki/A*_search_algorithm
g4 = DictGraph({'a': {'b': 1.5, 'e': 2},
                'b': {'c': 2},
                'c': {'d': 3},
                'd': {'g': 4},
                'e': {'f': 3},
                'f': {'g': 2},
                'g': {}})


def g4_heur(x):
    mapping = {'a': 6.5, 'b': 4, 'c': 2, 'd': 4, 'e': 4.5, 'f': 2, 'g': 0}
    return mapping.get(x)


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
    assert ['a'] == dijkstra(g3, 'a', lambda v: v == 'a')
    assert ['a', 'd', 'e'] == dijkstra(g3, 'a', lambda v: v == 'e')
    assert ['a', 'd', 'c', 'f'] == dijkstra(g3, 'a', lambda v: v == 'f')


def test_astar():
    assert ['a', 'e', 'f', 'g'] == astar(g4, 'a', lambda v: v == 'g', g4_heur)
