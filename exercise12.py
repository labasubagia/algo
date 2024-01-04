import unittest
from collections import defaultdict


class TestCase(unittest.TestCase):
    def test_add_until_100(self):
        arr = [x * 10 for x in range(11)]
        step_counter: defaultdict[str, int] = defaultdict(int)

        self.assertEqual(100, add_until_100(arr, step_counter))

        self.assertEqual(100, add_until_100_2(arr, step_counter))

        self.assertEqual(100, add_until_100_3(arr, step_counter))

        self.assertTrue(
            step_counter[add_until_100.__name__]
            >= step_counter[add_until_100_2.__name__]
            >= step_counter[add_until_100_3.__name__]
        )
        print(step_counter)

    def test_golomb(self):
        n = 10
        step_counter: defaultdict[str, int] = defaultdict(int)

        self.assertEqual(
            golomb(n, step_counter=step_counter), golomb2(n, step_counter=step_counter)
        )
        self.assertTrue(step_counter[golomb.__name__] > step_counter[golomb2.__name__])
        print(step_counter)

    def test_unique_paths(self):
        r, c = 5, 5
        step_counter: defaultdict[str, int] = defaultdict(int)

        self.assertEqual(
            unique_paths(r, c, step_counter=step_counter),
            unique_paths2(r, c, step_counter=step_counter),
        )
        print(step_counter)


def add_until_100(
    arr: list[int], step_counter: defaultdict[str, int] = defaultdict(int)
) -> int:
    step_counter[add_until_100.__name__] += 1
    if len(arr) == 0:
        return 0
    if arr[0] + add_until_100(arr[1 : len(arr)], step_counter) > 100:
        return add_until_100(arr[1 : len(arr)], step_counter)
    return arr[0] + add_until_100(arr[1 : len(arr)], step_counter)


# reduce recursive call
def add_until_100_2(
    arr: list[int], step_counter: defaultdict[str, int] = defaultdict(int)
) -> int:
    step_counter[add_until_100_2.__name__] += 1
    if len(arr) == 0:
        return 0

    agg = add_until_100_2(arr[1 : len(arr)], step_counter)
    if arr[0] + agg > 100:
        return agg
    return arr[0] + agg


# bottom-up iterative
def add_until_100_3(
    arr: list[int], step_counter: defaultdict[str, int] = defaultdict(int)
) -> int:
    ans = 0
    for x in arr:
        step_counter[add_until_100_3.__name__] += 1
        ans += x
        if ans >= 100:
            break
    return ans


def golomb(n: int, step_counter: defaultdict[str, int] = defaultdict(int)) -> int:
    step_counter[golomb.__name__] += 1
    if n == 1:
        return 1
    return 1 + golomb(
        n - golomb(golomb(n - 1, step_counter), step_counter), step_counter
    )


# use memoize
def golomb2(
    n: int,
    memo: dict[int, int] = {},
    step_counter: defaultdict[str, int] = defaultdict(int),
) -> int:
    step_counter[golomb2.__name__] += 1
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + golomb2(
            n
            - golomb2(
                golomb2(n - 1, memo, step_counter),
                memo,
                step_counter,
            ),
            memo,
            step_counter,
        )
    return memo[n]


def unique_paths(
    rows: int, cols: int, step_counter: defaultdict[str, int] = defaultdict(int)
) -> int:
    step_counter[unique_paths.__name__] += 1
    if rows == 1 or cols == 1:
        return 1
    return unique_paths(rows - 1, cols, step_counter) + unique_paths(
        rows, cols - 1, step_counter
    )


# use memoize
def unique_paths2(
    rows: int,
    cols: int,
    memo: dict[str, int] = {},
    step_counter: defaultdict[str, int] = defaultdict(int),
) -> int:
    step_counter[unique_paths2.__name__] += 1
    if rows == 1 or cols == 1:
        return 1

    key = f"{rows}_{cols}"
    if key not in memo:
        memo[key] = unique_paths2(rows - 1, cols, memo, step_counter) + unique_paths2(
            rows, cols - 1, memo, step_counter
        )

    return memo[key]


if __name__ == "__main__":
    unittest.main()
