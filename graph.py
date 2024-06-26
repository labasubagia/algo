from typing_extensions import Self
from collections import deque


class Vertex:
    def __init__(self, value: str) -> None:
        self.value = value
        self.adjacent_vertices: list[Self] = []

    def add_adjacent_vertex(self, vertex: Self) -> None:
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)


def dfs_traverse(vertex: Vertex, visited_vertices: dict[str, bool] = {}):
    visited_vertices[vertex.value] = True
    print(vertex.value)
    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value in visited_vertices:
            continue
        dfs_traverse(adjacent_vertex, visited_vertices)


def dfs_search(
    vertex: Vertex, search_value: str, visited_vertices: dict[str, bool] = {}
) -> Vertex | None:
    if vertex.value == search_value:
        return vertex
    visited_vertices[vertex.value] = True
    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value in visited_vertices:
            continue
        found = dfs_search(adjacent_vertex, search_value, visited_vertices)
        if found:
            return found
    return None


def bfs_traverse(vertex: Vertex):
    visited_vertices: dict[str, bool] = {}
    queue: deque[Vertex] = deque([vertex])
    while queue:
        current_vertex = queue.popleft()
        if current_vertex.value not in visited_vertices:
            visited_vertices[current_vertex.value] = True
            print(current_vertex.value)
        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value in visited_vertices:
                continue
            queue.append(adjacent_vertex)


def bfs_search(vertex: Vertex, search_value: str) -> Vertex | None:
    visited_vertices: dict[str, bool] = {}
    queue: deque[Vertex] = deque([vertex])
    while queue:
        current_vertex = queue.popleft()
        visited_vertices[current_vertex.value] = True
        if current_vertex.value == search_value:
            return current_vertex
        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value in visited_vertices:
                continue
            visited_vertices[adjacent_vertex.value] = True
            queue.append(adjacent_vertex)

    return None


if __name__ == "__main__":
    alice = Vertex("alice")
    bob = Vertex("bob")
    candy = Vertex("candy")
    derek = Vertex("derek")
    elaine = Vertex("elaine")
    fred = Vertex("fred")
    helen = Vertex("helen")
    gina = Vertex("gina")
    irena = Vertex("irena")

    alice.add_adjacent_vertex(bob)
    alice.add_adjacent_vertex(candy)
    alice.add_adjacent_vertex(derek)
    alice.add_adjacent_vertex(elaine)

    bob.add_adjacent_vertex(fred)
    fred.add_adjacent_vertex(helen)
    candy.add_adjacent_vertex(helen)

    derek.add_adjacent_vertex(elaine)
    derek.add_adjacent_vertex(gina)

    gina.add_adjacent_vertex(irena)

    dfs_traverse(alice)
    print()

    print(dfs_search(alice, "irena"))
    print(dfs_search(alice, "ilene"))
    print()

    bfs_traverse(alice)
    print()

    print(bfs_search(alice, "irena"))
    print(bfs_search(alice, "ilene"))
