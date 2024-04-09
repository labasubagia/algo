from typing_extensions import Self


class WeightedGraphVertex:
    def __init__(self, value: str) -> None:
        self.value = value
        self.adjacent_vertices: dict[Self, int] = {}

    def add_adjacent_vertex(self, vertex: Self, weight: int):
        self.adjacent_vertices[vertex] = weight


class City:
    def __init__(self, name: str) -> None:
        self.name = name
        self.routes: dict[Self, int] = {}

    def add_route(self, city: Self, price: int):
        self.routes[city] = price


def dijkstra_shortest_path(starting_city: City, final_destination: City):
    cheapest_table_price: dict[str, int] = {}
    cheapest_previous_stopover_city_table: dict[str, str] = {}

    visited_cities: set[str] = set()
    unvisited_cities: list[City] = [starting_city]

    cheapest_table_price[starting_city.name] = 0
    current_city = starting_city

    while current_city:
        visited_cities.add(current_city.name)
        unvisited_cities.remove(current_city)

        for adjacent_city, price in current_city.routes.items():
            if adjacent_city.name not in visited_cities:
                unvisited_cities.append(adjacent_city)

            price_through_current_city = cheapest_table_price[current_city.name] + price

            if (
                adjacent_city.name not in cheapest_table_price
                or price_through_current_city < cheapest_table_price[adjacent_city.name]
            ):
                cheapest_table_price[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.name] = (
                    current_city.name
                )

        current_city = (
            min(unvisited_cities, key=lambda city: cheapest_table_price[city.name])
            if unvisited_cities
            else None
        )

    shortest_path: list[str] = []
    current_city_name = final_destination.name
    while current_city_name != starting_city.name:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]

    shortest_path.append(starting_city.name)
    shortest_path.reverse()
    return shortest_path


if __name__ == "__main__":
    denver = City("denver")
    chicago = City("chicago")
    boston = City("boston")
    el_paso = City("el_paso")
    atlanta = City("atlanta")

    atlanta.add_route(boston, 100)
    atlanta.add_route(denver, 160)

    boston.add_route(chicago, 120)
    boston.add_route(denver, 180)

    chicago.add_route(el_paso, 80)

    denver.add_route(chicago, 40)
    denver.add_route(el_paso, 140)

    el_paso.add_route(boston, 100)

    print(dijkstra_shortest_path(atlanta, el_paso))
