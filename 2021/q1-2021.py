def is_pat(word: str) -> bool:
    if len(word) < 2:
        return True
    for m in range(1, len(word)):
        s1, s2 = word[:m], word[m:]
        if min([ord(c) for c in s1]) <= max([ord(c) for c in s2]):
            continue
          
        if is_pat(s1[::-1]) and is_pat(s2[::-1]):
            return True

    return False


[a, b] = input().split()
print("\n".join(map(lambda x: "YES" if is_pat(x) else "NO", [a, b, a + b])))
