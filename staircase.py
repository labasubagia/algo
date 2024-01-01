"""
question is to compute how many ways/path to climb staircase
when we can step on 1, 2 or 3 staircase in each step
"""


def number_of_paths(n: int) -> int:
    if n < 0:
        return 0
    if n <= 1:
        return 1
    return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)


if __name__ == "__main__":
    print(number_of_paths(5))
