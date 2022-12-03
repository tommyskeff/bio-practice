import string, math

def find_preference(arrangement: str, index: int) -> str:
    alphabet, layout, preferences = string.ascii_lowercase, [None] * len(arrangement), []
    for c in alphabet[:len(arrangement)]:
        position, permutations = arrangement.index(c), []
        for j in range(position):
            if layout[j]:
                permutations.append(j)
            else:
                permutations.clear()

        permutations.append(position)
        layout[position] = c
        preferences.append(sorted(permutations))
  
    lengths, permutation = list(map(len, preferences)), []
    for i, selection in enumerate(preferences):
        multiplied = math.prod(lengths[i + 1:])
        n = index // multiplied
        permutation.append(selection[n])
        index -= n * multiplied

    return "".join([alphabet[i].upper() for i in permutation])


[combination, index] = input().split()
print(find_preference(combination, int(index) - 1))
