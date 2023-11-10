def next_steps(n: str) -> list[str]:
    lst = []
    for i in range(0, len(n) - 1):
        a1 = n[i]
        a2 = n[i + 1]

        left_n = int(n[i - 1]) if i > 0 else -1
        right_n = int(n[i + 2]) if i + 2 < len(n) else -1

        k1 = int(a1 if int(a1) < int(a2) else a2)
        k2 = int(a2 if int(a1) < int(a2) else a1)

        if (left_n > k1 and left_n < k2) or (right_n > k1 and right_n < k2):
            new_string = list(n)
            new_string[i] = a2
            new_string[i + 1] = a1
            lst.append("".join(new_string))

    return lst





l = int(input())
n = input()

step = 1
tree = dict()
tree[n] = 0

while True:
    found = 0
    new_dict = dict()

    for key in tree.keys():
        vals = next_steps(str(key))

        for val in vals:
            if str(val) in tree or str(val) in new_dict:
                continue

            new_dict[str(val)] = step
            found += 1

    for k in new_dict.keys():
        tree[k] = new_dict[k]

    step += 1

    if found < 1:
        break


print(max(tree.values()))
