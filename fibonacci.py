def main():
    try:
        n = int(input("Number of terms (1-50): "))
    except ValueError:
        print("Invalid input. Enter a value from 1 to 50.")
        return 1

    if n < 1 or n > 50:
        print("Invalid input. Enter a value from 1 to 50.")
        return 1

    a, b = 0, 1
    terms = []
    for _ in range(n):
        terms.append(str(a))
        a, b = b, a + b

    print(" ".join(terms))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
