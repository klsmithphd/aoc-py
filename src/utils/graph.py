from functools import partial, reduce
from itertools import takewhile
from heapdict import heapdict
from math import inf
from toolz import assoc, iterate
from typing import Protocol


class Graph(Protocol):
    def vertices(self):
        """Return a collection of all the vertices"""
        pass

    def edges(self, v):
        """Return a collection of edges for the given vertex `v`"""
        pass

    def distance(self, v1, v2):
        """Return the distance (or edge weight) between two vertices `v1` and 
        `v2`"""
        pass


class DictGraph(Graph):
    """A Graph represented by a dict. The vertices of the graph are
    the keys of the dict. The values for each vertex are a sub-dict to
    represent the edges from that vertex, with the adjacent vertex as
    the key, and the distance (or edge weight) as the value.

    Ex: {'a': {'b': 2, 'c':10},
         'b': {'a': 2},
         'c': {'a': 10}}"""

    def __init__(self, d: dict):
        self.__d = d

    def __eq__(self, other) -> bool:
        return self.__d.__eq__(other._DictGraph__d)

    def vertices(self):
        return (v for v in self.__d)

    def edges(self, v):
        return (v2 for v2 in self.__d.get(v))

    def distance(self, v1, v2):
        return self.__d.get(v1).get(v2)


def isnotnone(x):
    return x is not None


def path_retrace(prev, finish):
    nodes = tuple(takewhile(isnotnone, iterate(lambda x: prev.get(x), finish)))
    return tuple(reversed(nodes))


def dijkstra_update(graph, vertex, state, neighbor):
    dist = state['dist']
    alt = dist.get(vertex) + graph.distance(vertex, neighbor)
    if (alt < dist.get(neighbor, inf)):
        state['dist'][neighbor] = alt
        state['queue'][neighbor] = alt
        state['prev'][neighbor] = vertex
    return state


def dijkstra(graph, start, istarget):
    state = {'dist': {start: 0},
             'prev': {},
             'queue': heapdict(start=0)}
    vertex = start
    visited = set()
    while (not (istarget(vertex)) and len(state['queue']) > 0):
        neighbors = (v for v in graph.edges(vertex) if v not in visited)
        updater = partial(dijkstra_update, graph, vertex)
        state = reduce(updater, neighbors, state)
        state['queue'].popitem()
        visited.add(vertex)
        vertex, _ = state['queue'].peekitem()
    return path_retrace(state['prev'], vertex)
