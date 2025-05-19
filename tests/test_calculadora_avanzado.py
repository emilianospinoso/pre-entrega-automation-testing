import pytest
from ..calculadora import sumar, restar, multiplicar, dividir

# ----- FIXTURES -----
@pytest.fixture
def numeros_enteros():
    """Prepara dos enteros comunes."""
    return 20, 5

@pytest.fixture
def numeros_decimales():
    """Prepara dos números decimales para pruebas de precisión."""
    return 0.1, 0.2

# ----- TESTS CON FIXTURES -----
def test_dividir_enteros(numeros_enteros):
    """Test que usa la fixture de números enteros para probar la división."""
    a, b = numeros_enteros
    assert dividir(a, b) == 4

def test_multiplicar_enteros(numeros_enteros):
    """Test que usa la fixture de números enteros para probar la multiplicación."""
    a, b = numeros_enteros
    assert multiplicar(a, b) == 100

# ----- TESTS PARAMETRIZADOS -----
@pytest.mark.parametrize(
    "a,b,esperado", 
    [
        (1, 2, 3),      # Enteros positivos
        (-1, -1, -2),   # Enteros negativos
        (2.5, 0.5, 3),  # Decimales
        (0, 0, 0)       # Caso cero
    ]
)
def test_sumar_varios(a, b, esperado):
    """Test parametrizado que prueba la función sumar con diversos valores."""
    assert sumar(a, b) == esperado

@pytest.mark.parametrize(
    "a,b,esperado", 
    [
        (10, 5, 5),     # Enteros positivos
        (-1, -2, 1),    # Enteros negativos
        (3.5, 1.5, 2),  # Decimales
        (0, 0, 0)       # Caso cero
    ]
)
def test_restar_varios(a, b, esperado):
    """Test parametrizado que prueba la función restar con diversos valores."""
    assert restar(a, b) == esperado

# ----- TESTS CON ETIQUETAS (MARKS) -----
@pytest.mark.smoke
def test_restar_smoke():
    """Test básico etiquetado como 'smoke' para pruebas rápidas."""
    assert restar(10, 8) == 2

@pytest.mark.smoke
def test_sumar_smoke():
    """Otro test etiquetado como 'smoke'."""
    assert sumar(5, 5) == 10

@pytest.mark.exception
def test_dividir_por_cero():
    """Test etiquetado como 'exception' que verifica manejo de error en división por cero."""
    with pytest.raises(ValueError) as excinfo:
        dividir(1, 0)
    # Verificamos también el mensaje de error
    assert "No se puede dividir por cero" in str(excinfo.value)

# ----- TESTS CON ASERCIONES DE PRECISIÓN -----
def test_multiplicar_preciso(numeros_decimales):
    """Test que verifica la precisión de multiplicación con números decimales."""
    a, b = numeros_decimales
    resultado = multiplicar(a, b)
    # Usando pytest.approx para comparación con tolerancia
    assert resultado == pytest.approx(0.02, abs=1e-8)

def test_dividir_preciso():
    """Test que verifica la precisión en división con resultado periódico."""
    resultado = dividir(1, 3)
    # Usando pytest.approx para comparación con tolerancia relativa
    assert resultado == pytest.approx(0.333333, rel=1e-4)