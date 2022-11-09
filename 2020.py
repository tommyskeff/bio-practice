NUMERALS = {
    1000: ["M"],
    500: ["D", "M"],
    100: ["C", "D"],
    50: ["L", "C"],
    10: ["X", "L"],
    5: ["V", "X"],
    1: ["I", "V"],
}


def to_numerals(n):
    s = ""
    for k, v in NUMERALS.items():
        if n >= k:
            r = n // k
            if r > 3:
                s += v[0] + v[1]
            else:
                s += v[0] * r

            n -= k * r

    return s


def represent(string):
    f, l, o = "", "", 0
    for c in string:
        if c == l:
            o += 1
            continue

        f += to_numerals(o) + l
        l, o = c, 1

    f += to_numerals(o) + l
    return f


def main():
    [s, n] = input().split()
    for i in range(int(n)):
        s = represent(s)

    a, b = 0, 0
    for c in s:
        if c == "I":
            a += 1
        elif c == "V":
            b += 1

    print(a, b)


main()
