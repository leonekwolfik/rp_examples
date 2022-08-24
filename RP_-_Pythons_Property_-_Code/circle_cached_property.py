# circle_cached_property.py

from functools import cached_property
from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def diameter(self):
        sleep(2)  # Simulate a costly computation
        return self.radius * 2


c = Circle(5)
print(c.diameter)
print(c.diameter)

c.radius = 15
print(c.diameter)
print(c.diameter)
