from functools import lru_cache

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@lru_cache(maxsize=len(ALPHA))
def generate_layer(layer_size: int) -> list[int]:
    if layer_size <= 1:
        return [1]

    prev_layer = generate_layer(layer_size - 1)
    output, total = [], 0

    for i in range(layer_size):
        if len(prev_layer) > i:
            total += prev_layer[i]
        output.append(total)

    return output


def count_chains(prefix: str, length: int) -> int:
    if len(prefix) == length:
        return 1
    elif len(prefix) < 1:
        return sum(generate_layer(length))
    elif len(prefix) > 1:
        ord_chars = list(map(ord, prefix[1:]))
        first_ord = ord(prefix[0])

        if first_ord < max(ord_chars) and first_ord < min(ord_chars):
            return 0

    layer_size = length - len(prefix) + 1
    char_index = ALPHA.index(prefix[-1])
    layer = generate_layer(layer_size)

    return layer[min(char_index, len(layer) - 1)]


l, p = input().split()
l = int(l)

answer = count_chains(p, l)
print(answer)
