"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0

#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
def test_mean_un_elemento():
    assert mean([5]) == 5.0

#   - Lista con números negativos
def test_mean_negativos():
    assert mean([-2, -4, -6]) == -4.0

#   - Lista con números decimales (float)
def test_mean_decimales():
    assert mean([1.5, 2.5, 3.5]) == pytest.approx(2.5)

#   - Lista vacía → debe lanzar ValueError
def test_mean_lista_vacia():
    with pytest.raises(ValueError):
        mean([])
# --- TU TURNO ---
# Agregá tests para los siguientes casos:
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])
