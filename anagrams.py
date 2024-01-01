def anagrams_of(string: str) -> list[str]:
    if len(string) == 1:
        return [string[0]]

    collection: list[str] = []

    substring_anagrams = anagrams_of(string[1 : len(string)])

    for substring_anagram in substring_anagrams:
        for index in range(len(substring_anagram)):
            copy = substring_anagram[:]
            collection.append(copy[:index] + string[0] + copy[index:])

    return collection


if __name__ == "__main__":
    print(anagrams_of("abcd"))
