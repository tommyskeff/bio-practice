COLOURS = ["R", "G", "B"]

def find_missing(a: str, b: str) -> str:
    if a == b: return a
    lst = COLOURS[:]
    lst.remove(a)
    lst.remove(b)
    return lst[0]

def find_square(row) -> str:
    for _ in range(len(row) - 1): row = [find_missing(c, row[i + 1]) for i, c in enumerate(row[:-1])]
    return row[0]

print(find_square(input()))