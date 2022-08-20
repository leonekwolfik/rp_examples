# try_parse1.py

def try_parse(string, base=10):
    try:
        return True, int(string, base=base)
    except ValueError:
        return False, None


values = ["", "160519", "9432.0", "16,667",
                        "   -322   ", "+4302", "(100);", "01FA" ]

for value in values:
    if try_parse(value)[0]:
        print(f"Converted {value} to {try_parse(value)[1]}")
    else:
        print(f"Attempted conversion of {value} failed")