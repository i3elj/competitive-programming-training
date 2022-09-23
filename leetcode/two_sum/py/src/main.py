def two_sum(arr: list[int], target: int) -> list[int]:
    looked = {}
    for k, v in enumerate(arr):
        diff = target - v
        if diff in looked:
            return [looked[diff], k]
        looked[v] = k

    # answer = [k for k, v in enumerate(arr) if (target - v) in arr[1::]]
    # return answer


def main():
    # print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([2, 4, 3], 6))


if __name__ == "__main__":
    main()
