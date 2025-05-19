
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

# Menú interactivo

def calculadora():
    print("\n--- CALCULADORA PYTHON ---")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print("1) Sumar  2) Restar  3) Multiplicar  4) Dividir")
    opcion = input("Elije (1-4): ")
    try:
        if opcion == '1': resultado = sumar(a, b)
        elif opcion == '2': resultado = restar(a, b)
        elif opcion == '3': resultado = multiplicar(a, b)
        elif opcion == '4': resultado = dividir(a, b)
        else:
            print("Opción inválida.")
            return
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    calculadora()
