# greeting2.py

def greet(name, counter):
    return f"Hi, {name}!", counter + 1

count = 0

print(greet("Alice", count))
print(f"Count is {count}")
print(greet("Bob", count))
print(f"Count is {count}")