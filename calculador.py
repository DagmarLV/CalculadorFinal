def multiplicar(num1, num2):
    return num1 * num2

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado

    except ZeroDivisionError:
        raise ZeroDivisionError("El divisor no puede ser cero")

if __name__ == "__main__":
    num1 = float(input())
    num2 = float(input())
    print(f"Suma: {sumar(num1, num2)}")
    print(f"Resta: {restar(num1, num2)}")
    print(f"Multiplicación: {multiplicar(num1, num2)}")
    print(f"División: {dividir(num1, num2)}")
