import random  # Importa el módulo random para poder seleccionar elementos aleatorios.

# Lista de algunos números romanos.
numeros_romanos = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", 
                   "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C", "CI", "CII", "CIV", "CIX"]

# Selección aleatoria de un número romano de la lista.
romano = random.choice(numeros_romanos)

def convertir_romano_a_entero(romano):
    # Diccionario que mapea los símbolos romanos a sus valores enteros.
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0  # Inicializa el total acumulado a 0.
    previo = 0  # Inicializa el valor previo a 0 para el procesamiento de símbolos.
    
    # Itera sobre los símbolos del número romano en orden inverso.
    for simbolo in reversed(romano):
        valor = valores[simbolo]  # Obtiene el valor entero del símbolo actual.
        
        if valor < previo:  # Si el valor actual es menor que el valor previo,
            total -= valor  # se resta del total (maneja la notación de resta en números romanos).
        else: 
            total += valor  # Si no, se suma al total.
        
        previo = valor  # Actualiza el valor previo al valor actual.
    
    return total  # Retorna el valor entero total calculado.

# Imprime el número romano seleccionado y su conversión a entero.
print(f"Número romano: {romano}")
print(f"Convertido a entero: {convertir_romano_a_entero(romano)}")

#Andres
