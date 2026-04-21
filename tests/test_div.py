"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0

#   - División que da resultado decimal (float)
def test_div_decimal():
    assert div(5, 2) == pytest.approx(2.5)

#   - División con números negativos
def test_div_negativos():
    assert div(-6,3) == -2.0
    assert div( 6, -3) == -2.0
    assert div(-6, -3) == 2.0

#   - División por cero → debe lanzar ZeroDivisionError
def test_div_por_cero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

# --- TU TURNO ---
# Agregá tests para los siguientes casos:
# Pista: para testear excepciones usá pytest.raises:
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)
