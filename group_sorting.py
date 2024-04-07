# sort per group in any order
# ababab  -> aaabbb or bbbaaa


# nlogn
def group_sort1(arr: list[str]) -> list[str]:
    return sorted(arr)


# n
def group_sort2(arr: list[str]) -> list[str]:
    m: dict[str, int] = {}
    for c in arr:
        if c not in m:
            m[c] = 0
        m[c] += 1

    ans: list[str] = []
    for k in m:
        for _ in range(m[k]):
            ans.append(k)
    return ans


if __name__ == "__main__":
    arr = ["a", "b", "a", "c", "b", "c", "d", "e", "d"]
    print(group_sort1(arr.copy()))
    print(group_sort2(arr.copy()))
