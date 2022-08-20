# try_parse2.py

def try_parse(string, base=10):
    try:
        return True, int(string, base=base)
    except ValueError:
        return False, None


values = ["", "160519", "9432.0", "16,667",
                        "   -322   ", "+4302", "(100);", "01FA" ]

for value in values:
    success, number = try_parse(value)
    if success:
        print(f"Converted {value} to {number}")
    else:
        print(f"Attempted conversion of {value} failed")