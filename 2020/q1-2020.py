import re

numerals, b = "MDCLXVI", []
for i in range(7): b.append((b[i - 1] if i else 5000) // (2 if i % 2 else 5))

def convert_numerals(n: int, f="") -> str:
    while n > 0:
        u = max([k if k <= n else 0 for k in b])
        a, i = n // u, b.index(u)
        n -= a * u
        f += numerals[i] + (numerals[i - 1] if a > 3 else numerals[i] * (a - 1))
    return f

def search_numeral(n: str, i: int) -> tuple:
    for _ in range(int(i)): n = "".join([convert_numerals(len(w)) + q for [w, q] in re.findall(r'((\w)\2*)', n)])
    return sum([1 if c == numerals[6] else 0 for c in n]), sum([1 if c == numerals[5] else 0 for c in n])

[n, i] = input().split()
print(" ".join(map(str, search_numeral(n, i))))
