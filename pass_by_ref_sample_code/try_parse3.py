# try_parse3.py

def try_parse(string, base=10):
    try:
        return int(string, base=base)
    except ValueError:
        return None


values = ["", "160519", "9432.0", "16,667",
                        "   -322   ", "+4302", "(100);", "01FA" ]

for value in values:
    if (number := try_parse(value)) is not None:
        print(f"Converted {value} to {number}")
    else:
        print(f"Attempted conversion of {value} failed")