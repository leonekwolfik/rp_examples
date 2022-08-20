# greeting3.py

def greet(name, counter):
    return f"Hi, {name}!", counter + 1

count = 0

greeting, count = greet("Alice", count)
print(f"{greeting}")
print(f"Count is {count}")

greeting, count = greet("Bob", count)
print(f"{greeting}")
print(f"Count is {count}")