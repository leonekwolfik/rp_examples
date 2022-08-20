# greeting1.py

def greet(name, counter):
    counter += 1
    return f"Hi, {name}!"

count = 0

print(greet("Alice", count))
print(f"Count is {count}")
print(greet("Bob", count))
print(f"Count is {count}")