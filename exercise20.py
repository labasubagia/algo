import unittest


# Q1
def player_with_multiple_sports(
    basketball_players: list[dict[str, str]], football_players: list[dict[str, str]]
) -> list[str]:
    set_basketball_player: set[str] = set()
    for player in basketball_players:
        set_basketball_player.add(f"{player['first_name']} {player['last_name']}")

    players: list[str] = []
    for player in football_players:
        full_name = f"{player['first_name']} {player['last_name']}"
        if full_name in set_basketball_player:
            players.append(full_name)
    return players


# Q2
# guaranteed always one missing
# n is len
def find_missing_in_0_until_n(nums: list[int]) -> int:
    n = len(nums)
    sum_target = n * (n + 1) // 2
    sum_current = sum(nums)
    return sum_target - sum_current


# Q3
# info: using greedy
def stock_max_profit(prices: list[float]) -> float:
    buy_price = prices[0]
    max_profit = 0
    for price in prices:
        current_profit = price - buy_price
        if price < buy_price:
            buy_price = price
        max_profit = max(max_profit, current_profit)
    return max_profit


# Q4
def max_product_two_number(nums: list[int]) -> int:
    smallest = second_smallest = float("inf")
    largest = second_largest = float("-inf")
    for n in nums:
        if n <= smallest:
            second_smallest = smallest
            smallest = n
        elif n > smallest and n < second_smallest:
            second_smallest = n
        if n >= largest:
            second_largest = largest
            largest = n
        elif n < largest and n > second_largest:
            second_largest = n

    largest_product = largest * second_largest
    smallest_product = smallest * second_smallest
    return max(int(smallest_product), int(largest_product))


# Q5 Answer 1
def sort_temperature(nums: list[float]) -> list[float]:
    # limit from 97.0 until 99.0, total 21 numbers
    # Fahrenheit decimal 1-9, one digit
    temperatures = [0] * 21
    for n in nums:
        pos = int(n * 10) - 970
        temperatures[pos] += 1

    res: list[float] = []
    for i in range(len(temperatures)):
        for _ in range(temperatures[i]):
            n = (970 + i) / 10
            res.append(n)
    return res


# Q6
def longest_sequence_length(nums: list[int]) -> int:
    hash_map: set[int] = set()
    longest_length = 0

    for number in nums:
        hash_map.add(number)

    for number in nums:
        if number - 1 not in hash_map:
            length = 1
            current_number = number
            while current_number + 1 in hash_map:
                current_number += 1
                length += 1
                longest_length = max(longest_length, length)
    return longest_length


class TestCase(unittest.TestCase):
    def test_player_with_multiple_sports(self):
        basketball_players = [
            {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
            {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
            {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
            {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
            {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"},
        ]
        football_players = [
            {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
            {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
            {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
            {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
            {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"},
        ]
        expected = ["Jill Huang", "Wanda Vakulskas"]
        self.assertEqual(
            expected, player_with_multiple_sports(basketball_players, football_players)
        )

    def test_find_missing_in_0_until_n(self):
        self.assertEqual(4, find_missing_in_0_until_n([2, 3, 0, 6, 1, 5]))
        self.assertEqual(1, find_missing_in_0_until_n([8, 2, 3, 9, 4, 7, 5, 0, 6]))

    def test_stock_max_profit(self):
        self.assertEqual(6.0, stock_max_profit([10, 7, 5, 8, 11, 2, 6]))

    def test_max_product(self):
        test_cases = [
            ([5, -10, -6, 9, 4], 60),
            ([5, 9, 4], 45),
            ([0, 0], 0),
            ([-3, -2], 6),
        ]
        for nums, expected in test_cases:
            self.assertEqual(expected, max_product_two_number(nums))

    def test_sort_temperatures(self):
        arr = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
        expected = sorted(arr)

        actual = sort_temperature(arr)
        self.assertEqual(expected, actual)

    def test_longest_sequence_length(self):
        test_cases = [
            ([10, 5, 12, 3, 55, 30, 4, 11, 2], 4),
            ([19, 13, 15, 12, 18, 14, 17, 11], 5),
        ]
        for nums, expected in test_cases:
            self.assertEqual(expected, longest_sequence_length(nums))


if __name__ == "__main__":
    unittest.main()
