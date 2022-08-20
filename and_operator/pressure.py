# pressure.py

from time import sleep
from random import randint

def control_pressure():
    pressure = measure_pressure()
    while True:
        if pressure <= 500:
            break

        while pressure > 500 and pressure <= 700:
            run_standard_safeties()
            pressure = measure_pressure()

        while pressure > 700:
            run_critical_safeties()
            pressure = measure_pressure()

    print("Wow! The system is safe...")

def measure_pressure():
    pressure = randint(490, 800)
    print(f"psi={pressure}", end="; ")
    return pressure

def run_standard_safeties():
    print("Running standard safeties...")
    sleep(0.2)

def run_critical_safeties():
    print("Running critical safeties...")
    sleep(0.7)

if __name__ == "__main__":
    control_pressure()