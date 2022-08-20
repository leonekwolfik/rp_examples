# attributes.py

from types import SimpleNamespace

ns = SimpleNamespace()

def square(instance):
    instance.n *= instance.n

ns.n = 4
square(ns)
ns.n