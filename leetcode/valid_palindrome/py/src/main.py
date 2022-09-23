def is_palindrome(s: str) -> bool:
    s = ''.join(c for c in s if c.isalnum()).lower()
    return True if s[::-1] == s else False


def main():
    print(is_palindrome("A man, a plan, a canal: Panama"))


if __name__ == "__main__":
    main()
