from itertools import takewhile
from heapdict import heapdict
from math import inf
from toolz import iterate
from typing import Protocol
from utils.core import isnotnone


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


def path_retrace(prev, finish):
    """Helper function for graph traversal algorithms that returns a
    sequence of nodes along a path, given `prev`, a dict that maps
    each node to its previous node along a preferred path, and `finish`,
    the endpoint of the path."""
    if (len(prev) == 0):
        return [finish]
    else:
        nodes = list(takewhile(isnotnone, iterate(
            lambda x: prev.get(x), finish)))
        return list(reversed(nodes))


def dijkstra(graph: Graph, start, istarget):
    """Using Dijkstra's algorith, returns the shortest path in `graph`,
    from `start` until the function `istarget` evaluated against a node
    returns True.

    If a path cannot be found, returns `None`.
    """

    # tentative distance to each node. Initially, we only know the start node
    dist = {start: 0}

    # a dict mapping nodes to the previous node on the shortest-hop path
    # discovered so far
    prev = {}

    # A Priority Queue (here implemented by a heapdict) for the next nodes
    # to examine.
    queue = heapdict({start: 0})

    # The next node to visit
    vertex = start

    # The set of nodes visited thus far
    visited = set()
    while (not (istarget(vertex)) and len(queue) > 0):
        vertex, _ = queue.popitem()
        for neighbor in (v for v in graph.edges(vertex) if v not in visited):
            # alt is the distance from the start node to the neighbor
            # node if we go through vertex
            alt = dist.get(vertex) + graph.distance(vertex, neighbor)

            # If alt is shorter than the current known distance to neighbor
            # (or infinity if unknown), update our records with this newly
            # discovered shorter path
            if (alt < dist.get(neighbor, inf)):
                dist[neighbor] = alt
                queue[neighbor] = alt
                prev[neighbor] = vertex
        visited.add(vertex)

    return path_retrace(prev, vertex) if istarget(vertex) else None


def astar(graph: Graph, start, istarget, heuristic):
    """Using the A* algorithm, returns the shortest path in `graph`
    from `start` until the function `istarget` evaluated against a node
    returns true, using the `heuristic` function to guide the path-finding.
    The heuristic function should accept a single argument (a node in the
    graph) and should estimate the cost of reaching the target destination.

    If a path to the target cannot be found, returns `None`"""

    # tentative distance to each node. Initially, we only know the start node
    dist = {start: 0}

    # a dict mapping nodes to the previous node on the shortest-hop path
    # discovered so far
    prev = {}

    # A Priority Queue (here implemented by a heapdict) for the next nodes
    # to examine.
    queue = heapdict({start: heuristic(start)})

    # The next node to visit
    vertex = start
    while (not (istarget(vertex)) and len(queue) > 0):
        vertex, _ = queue.popitem()
        for neighbor in (v for v in graph.edges(vertex)):
            # alt is the distance from the start node to the neighbor
            # node if we go through vertex
            alt = dist.get(vertex) + graph.distance(vertex, neighbor)

            # If alt is shorter than the current known distance to neighbor
            # (or infinity if unknown), update our records with this newly
            # discovered shorter path
            if (alt < dist.get(neighbor, inf)):
                dist[neighbor] = alt
                queue[neighbor] = alt + heuristic(neighbor)
                prev[neighbor] = vertex

    return path_retrace(prev, vertex) if istarget(vertex) else None
