"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8

#   - Cualquier número elevado a 0 (resultado: 1)
def test_pow_exponente_cero():
    assert pow_(5, 0) == 1

#   - Número elevado a 1 (resultado: el mismo número)
def test_pow_exponente_uno():
    assert pow_(7, 1) == 7

#   - Base negativa con exponente par (resultado positivo)
def test_pow_base_negativa_exponente_par():
    assert pow_(-2, 4) == 16

#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
def test_pow_exponente_decimal():
    assert pow_(9, 0.5) == pytest.approx(3.0)

# Agregá tests para los siguientes casos:
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
