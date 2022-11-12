import collections
import time

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def add_window(state: tuple) -> tuple:
    window, warehouse, distance = state
    return window + warehouse[0], warehouse[1:], distance + 1


def rotate_window(state: tuple) -> tuple:
    window, warehouse, distance = state
    return window[1:] + window[0], warehouse, distance + 1


def swap_window(state: tuple) -> tuple:
    window, warehouse, distance = state
    window = list(window)
    window[0], window[1] = window[1], window[0]
    return "".join(window), warehouse, distance + 1


def call(func, permutation, target, perms, dm):
    permutation = func(permutation)
    window, distance = permutation[0], permutation[2]

    if window == target:
        return distance

    if distance < dm[window]:
        dm[window] = distance
        perms.append(permutation)


def solve(target: str) -> int:
    distance_memory, solution = collections.defaultdict(lambda: 9999), None
    permutations, permutation = collections.deque([("", ALPHABET[:len(target)], 0)]), ""
    execute = lambda func: call(func, permutation, target, permutations, distance_memory)

    while not solution and permutations:
        permutation = permutations.popleft()
        if len(permutation[1]):
            result = execute(add_window)
            if result: solution = result

        if len(permutation[0]) > 1:
            result = execute(swap_window)
            if result: solution = result

            result = execute(rotate_window)
            if result: solution = result

    return solution


print(solve(input()))
