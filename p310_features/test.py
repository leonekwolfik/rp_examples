def greet(name):
    match name:
        case "Guido":
            print("I'm not worthy")
        case _:
            print(f"Hello {name}")


greet('Chris')
greet('Guido')