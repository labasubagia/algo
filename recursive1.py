"""
recursive 1
get direct & indirect related products
"""

import unittest
from typing import List, Set


class TestCase(unittest.TestCase):
    def test_related_1(self):
        products = [
            ["AB", "A"],
            ["AB", "B"],
            ["BC", "B"],
            ["BC", "C"],
            ["DE", "D"],
            ["DE", "E"],
        ]

        test_cases = [
            ("AB", ["AB", "A", "B", "BC", "B", "C"]),
            ("E", ["DE", "D", "E"]),
            ("C", ["AB", "A", "B", "BC", "B", "C"]),
        ]

        for target, expected in test_cases:
            result = get_related_product_recursive(products, target)
            self.assertEqual(sorted(result), sorted(set(expected)))

    def test_related_2(self):
        products = [
            ["AB", "A"],
            ["AB", "B"],
            ["CD", "C"],
            ["CD", "D"],
            ["EF", "E"],
            ["EF", "F"],
        ]

        test_cases = [
            ("B", ["AB", "A", "B"]),
            ("CD", ["CD", "C", "D"]),
            ("F", ["EF", "E", "F"]),
        ]

        for target, expected in test_cases:
            result = get_related_product_recursive(products, target)
            self.assertEqual(sorted(result), sorted(set(expected)))


def get_related_product_recursive(
    products: List[List[str]], target_product: str, visited: Set[str] | None = None
) -> Set[str]:
    """
    get_related_data_recursive
    this fn is for get all related product [[bundle, component],...]
    find the direct and indirect relation to a product
    """

    if visited is None:
        visited = set()

    related_data: Set[str] = set()

    for bundle, component in products:
        if bundle == target_product and component not in visited:
            visited.add(component)
            related_data.add(component)
            related_data |= get_related_product_recursive(products, component, visited)
        elif component == target_product and bundle not in visited:
            visited.add(bundle)
            related_data.add(bundle)
            related_data |= get_related_product_recursive(products, bundle, visited)

    return related_data


if __name__ == "__main__":
    unittest.main()
