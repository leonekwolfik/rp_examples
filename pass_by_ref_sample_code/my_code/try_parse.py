def try_parse(string, base=10):
    try:
        return int(string, base=base)
    except ValueError:
        return None


for value in ("", "23452345", "4356.0", "345,345", "    -234", "+345", "(1234)", "01FA"):
    if number := try_parse(value):
        print(f"Converted {value=} to {number=}")
    else:
        print(f"Attempted conversion of {value=} failed.")

