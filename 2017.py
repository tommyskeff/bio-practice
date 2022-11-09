COLOURS = ["R", "G", "B"]


def calc_row(r1):
    r2 = []
    for i in range(len(r1) - 1):
        i1, i2, b = r1[i], r1[i + 1], ""
        if i1 == i2:
            b = i1
        else:
            for c in COLOURS:
                if (not i1 == c) and (not i2 == c):
                    b = c

        r2.append(b)

    return r2


def main():
    row, go, ans = list(input()), True, ""
    while go:
        if len(row) < 2:
            go = False
            ans = row

        row = calc_row(row)

    print(ans[0])


main()
