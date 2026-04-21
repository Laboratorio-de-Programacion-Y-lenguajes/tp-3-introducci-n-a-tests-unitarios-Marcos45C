"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3

def test_add_suma_negativos():
    assert add(-1,-1)==-2

def test_add_suma_positivo_negativo():
    assert add(-1,1)==0
def test_add_suma_cero():
    assert add(0,0)==0
def test_add_suma_decimales():
    assert add(2.1, 2.1) == pytest.approx(4.2)
# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos°
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected
