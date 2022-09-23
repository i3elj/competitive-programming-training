
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    for i in range(len(t)):
        if s[i] != t[i]:
            return False
    else:
        return True


def main():
    print(is_anagram("hello", "hleol"))


if __name__ == "__main__":
    main()
