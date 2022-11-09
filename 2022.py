def decrypt(word):
    word = list(word)
    for i in range(len(word) - 1, 0, -1):
        dp = ord(word[i]) - ord(word[i - 1])
        if dp < 1:
            dp += 26

        word[i] = chr(dp + 64)

    return "".join(word)


def main():
    print(decrypt(input()))


if __name__ == "__main__":
    main()
