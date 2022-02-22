def calculate_triples(n):
    array = [(a, b, c) for a in range(1, n)
             for b in range(a, n)
             for c in range(b, n) if (a ** 2 + b ** 2) == c ** 2]
    return array


if __name__ == "__main__":
    n = int(input("Please enter number: "))
    print(calculate_triples(n))

