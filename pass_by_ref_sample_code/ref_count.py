# ref_count.py

from sys import getrefcount

print("--- Before  assignment ---")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")

x = "value_1"
print("--- After   assignment ---")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")

x = "value_2"
print("--- After reassignment ---")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")