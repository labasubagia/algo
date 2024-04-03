from typing_extensions import Self


class Vertex:
    def __init__(self, value: str) -> None:
        self.value = value
        self.adjacent_vertices: list[Self] = []

    def add_adjacent_vertex(self, vertex: Self) -> None:
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)


if __name__ == "__main__":
    alice = Vertex("alice")
    bob = Vertex("bob")
    cynthia = Vertex("cynthia")

    alice.add_adjacent_vertex(bob)
    alice.add_adjacent_vertex(cynthia)

    bob.add_adjacent_vertex(cynthia)
    cynthia.add_adjacent_vertex(bob)
    print(vars(cynthia))
