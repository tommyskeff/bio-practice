ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def product(lst: list, f=1) -> int:
    for n in lst:
        f *= n
    return f


def find_preference(arrangement: str, index: int) -> str:
    index -= 1
    preferences = []
    length = len(arrangement)
    layout = [None] * length

    for i in range(length):
        letter, permutations = ALPHABET[i].lower(), []
        position = arrangement.index(letter)

        for j in range(position):
            if layout[j] == None:
                permutations.clear()
            else:
                permutations.append(j)

        permutations.append(position)
        layout[position] = letter
        preferences.append(sorted(permutations))

    lengths, permutation = list(map(len, preferences)), []
    for i in range(length):
        multiplied = product(lengths[i + 1:])
        n = index // multiplied
        permutation.append(preferences[i][n])
        index -= n * multiplied

    return "".join([ALPHABET[i] for i in permutation])


[combination, index] = input().split()
print(find_preference(combination, int(index)))
