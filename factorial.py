def main():
    try:
        n = int(input("Enter n (0-20): "))
    except ValueError:
        print("Invalid input. Enter an integer from 0 to 20.")
        return 1

    if n < 0 or n > 20:
        print("Invalid input. Enter an integer from 0 to 20.")
        return 1

    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    print(f"{n}! = {factorial}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
