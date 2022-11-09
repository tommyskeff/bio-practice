def is_pat(word):
    if len(word) < 2:
        return True

    for m in range(1, len(word)):
        s1, s2 = word[:m], word[m:]

        if min([ord(c) for c in s1]) <= max([ord(c) for c in s2]):
            continue

        if is_pat(s1[::-1]) and is_pat(s2[::-1]):
            return True

    return False


def swap_bool(b):
    return "YES" if b else "NO"


def main():
    [a, b] = input().split()
    print(swap_bool(is_pat(a)))
    print(swap_bool(is_pat(b)))
    print(swap_bool(is_pat(a + b)))


main()
