ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cache = {}


def count_permutations(alpha_length: int, max_permitted: int, remaining: int, last_char: str, last_char_count: int) -> int:
    if last_char_count and last_char_count > max_permitted:
        return 0
    
    if remaining <= 0:
        return 1

    hashed_args = hash((alpha_length, max_permitted, remaining, last_char, last_char_count))
    if hashed_args in cache:
        return cache[hashed_args]

    total = 0
    for i in range(alpha_length):
        same_char = last_char == i
        if same_char and not last_char_count < max_permitted:
            continue

        total += count_permutations(alpha_length, max_permitted, remaining - 1, i, last_char_count + 1 if same_char else 1)

    cache[hashed_args] = total
    return total


def find_plan(alpha_length: int, max_permitted: int, length: int, plan: int) -> str:
    solution = ""
    last_char, last_char_count = None, 0
    for i in range(length):
        for j in range(alpha_length):
            new_last_char_count = last_char_count + 1 if j == last_char else 1
            permutations = count_permutations(alpha_length, max_permitted, length - i - 1, j, new_last_char_count)
            if permutations >= plan:
                solution += ALPHABET[j]
                last_char, last_char_count = j, new_last_char_count
                break
            
            plan -= permutations
                
    return solution


[p, q, r], n = map(int, input().split()), int(input())
print(find_plan(p, q, r, n))