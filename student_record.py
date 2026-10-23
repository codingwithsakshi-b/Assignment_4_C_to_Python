def main():
    try:
        roll_no = int(input("Roll number: "))
    except ValueError:
        return 1

    name = input("Name: ")
    if not name or len(name) > 49:
        return 1

    try:
        marks = float(input("Marks (0-100): "))
    except ValueError:
        print("Invalid marks.")
        return 1

    if marks < 0 or marks > 100:
        print("Invalid marks.")
        return 1

    print(f"Roll: {roll_no}\nName: {name}\nMarks: {marks:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
