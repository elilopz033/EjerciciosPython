'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''


def calcular_area(poligono):
    tipo = poligono.get("tipo")  # Obtener el tipo del polígono

    if tipo == "Triángulo":
        base = poligono.get("base")
        altura = poligono.get("altura")
        if base is None or altura is None:
            return "Datos incompletos para calcular el área de un Triángulo."
        area = (base * altura) / 2
        print(f"El área del Triángulo es: {area}")
        return area

    elif tipo == "Cuadrado":
        lado = poligono.get("lado")
        if lado is None:
            return "Datos incompletos para calcular el área de un Cuadrado."
        area = lado ** 2
        print(f"El área del Cuadrado es: {area}")
        return area

    elif tipo == "Rectángulo":
        base = poligono.get("base")
        altura = poligono.get("altura")
        if base is None or altura is None:
            return "Datos incompletos para calcular el área de un Rectángulo."
        area = base * altura
        print(f"El área del Rectángulo es: {area}")
        return area

    else:
        return "Tipo de polígono no soportado."

# Ejemplo de uso:
# Triángulo
calcular_area({"tipo": "Triángulo", "base": 5, "altura": 8})

# Cuadrado
calcular_area({"tipo": "Cuadrado", "lado": 4})

# Rectángulo
calcular_area({"tipo": "Rectángulo", "base": 6, "altura": 3})
