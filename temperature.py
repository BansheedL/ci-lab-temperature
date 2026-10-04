ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    if c < ABSOLUTE_ZERO_C:
        raise ValueError("Температура не може бути нижчою за абсолютний нуль")
    return c - ABSOLUTE_ZERO_C
