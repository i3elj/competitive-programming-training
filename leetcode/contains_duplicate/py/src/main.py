def contains_duplicate(arr: [int]) -> bool:
    table = set()
    for i in arr:
        if i in table:
            return True
        table.add(i)
    return False


def main():
    print(contains_duplicate([1, 2, 3, 2, 4]))


if __name__ == "__main__":
    main()
