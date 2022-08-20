# short_circuit.py

# a pair of functions to demonstrate Python's
# use of short-circuit evaluation

def true_func():
    print("Running true_func()")
    return True

def false_func():
    print("Running false_func()")
    return False

print(true_func() or false_func())