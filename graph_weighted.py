from typing_extensions import Self


class WeightedGraphVertex:
    def __init__(self, value: str) -> None:
        self.value = value
        self.adjacent_vertices: dict[Self, int] = {}

    def add_adjacent_vertex(self, vertex: Self, weight: int):
        self.adjacent_vertices[vertex] = weight


class City(WeightedGraphVertex):
    pass


if __name__ == "__main__":
    denver = City("denver")
    chicago = City("chicago")
    boston = City("boston")
    el_paso = City("el_paso")
    atlanta = City("atlanta")

    denver.add_adjacent_vertex(chicago, 40)
    denver.add_adjacent_vertex(el_paso, 140)

    chicago.add_adjacent_vertex(el_paso, 80)

    el_paso.add_adjacent_vertex(boston, 100)

    atlanta.add_adjacent_vertex(boston, 100)
    atlanta.add_adjacent_vertex(denver, 160)
