from ..calculadora import sumar, restar, multiplicar, dividir
import pytest

def test_sumar_positivo():
    assert sumar(2, 3) == 5

def test_sumar_negativo():
    assert sumar(-2, -3) == -5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(1, 0)
