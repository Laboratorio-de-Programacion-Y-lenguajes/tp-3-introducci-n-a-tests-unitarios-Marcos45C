"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12

#   - Multiplicar por cero
def test_mul_por_cero():
    assert mul(5, 0) == 0

#   - Multiplicar dos números negativos (resultado positivo)
def test_mul_negativos():
    assert mul(-3, -2) == 6


#   - Multiplicar un positivo y un negativo (resultado negativo)
def test_mul_mixto():
    assert mul(3, -2) == -6


#   - Multiplicar por 1 (elemento neutro)
def test_mul_por_uno():
    assert mul(7, 1) == 7

#   - Multiplicar dos decimales (float)
def test_mul_decimales():
    assert mul(2.5, 2.0) == pytest.approx(5.0)


#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
