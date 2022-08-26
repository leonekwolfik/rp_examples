# pattern/match_class.py
from dataclasses import dataclass

@dataclass
class Mouse:
    position: tuple

@dataclass
class Keyboard:
    key: str

def show_event(event):
    match event:
        case Mouse((x, y)):
            print(f"Mouse click at {x},{y}")
        case Keyboard(key) as k:
            print(f"Key pressed was {k.key}")
