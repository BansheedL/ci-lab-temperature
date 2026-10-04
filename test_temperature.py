import pytest
from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6)


def test_celsius_to_fahrenheit_negative():
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(-10) == 14


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(0) == pytest.approx(-17.7778, rel=1e-4)


def test_round_trip():
    for c in (-273.15, -40, 0, 25.5, 100):
        f = celsius_to_fahrenheit(c)
        assert fahrenheit_to_celsius(f) == pytest.approx(c)


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == pytest.approx(273.15)
    assert celsius_to_kelvin(100) == pytest.approx(373.15)
    assert celsius_to_kelvin(-100) == pytest.approx(173.15)


def test_celsius_to_kelvin_absolute_zero():
    assert celsius_to_kelvin(-273.15) == 0


def test_celsius_to_kelvin_below_absolute_zero():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-300)
