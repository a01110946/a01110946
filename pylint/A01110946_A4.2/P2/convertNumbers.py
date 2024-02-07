"""
convertNumbers.py

Módulo diseñado para leer números de uno o varios archivos de texto, convertir
cada número a sus representaciones binaria y hexadecimal, y luego imprimir y
guardar los resultados en una tabla comparativa usando la biblioteca tabulate.
Los resultados se muestran tanto en la consola como en un archivo denominado
'ConversionResults.txt' para cada archivo de entrada procesado. Este script
maneja errores para datos no numéricos y archivos no encontrados, y registra
el tiempo total de ejecución para el procesamiento de cada archivo.

Uso: python convertNumbers.py archivo_con_numeros1.txt [archivo_con_numeros2.txt ...]

Autor: Fernando Maytorena
"""

import sys
import time
from tabulate import tabulate

def read_numbers(file_path):
    """Lee números de un archivo y devuelve una lista de enteros."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Error: '{line.strip()}' no es un número válido. Se omite.")
        return numbers
    except FileNotFoundError as e:
        print(f"Error al leer el archivo: {e}")
        return []

def convert_numbers(numbers):
    """Convierte los números a representaciones binaria y hexadecimal."""
    conversions = [{'Decimal': n, 'Binario': bin(n), 'Hexadecimal': hex(n)} for n in numbers]
    return conversions

def process_files(file_paths):
    """Procesa múltiples archivos y recolecta las conversiones."""
    conversions_list = []
    for file_path in file_paths:
        start_time = time.time()
        numbers = read_numbers(file_path)
        conversions = convert_numbers(numbers)
        elapsed_time = time.time() - start_time
        conversions_list.append((file_path, conversions, elapsed_time))
    return conversions_list

def print_comparative_table(all_conversions):
    """Imprime los resultados en una tabla comparativa con tabulate, y los guarda en un archivo."""
    table = []
    for file_path, conversions, elapsed_time in all_conversions:
        for conversion in conversions:
            table.append([file_path, conversion['Decimal'], conversion['Binario'],
                          conversion['Hexadecimal'], f"{elapsed_time:.4f} s"])

    headers = ["Archivo", "Decimal", "Binario", "Hexadecimal", "Tiempo Transcurrido"]
    table_str = tabulate(table, headers=headers, tablefmt="pretty")
    print(table_str)

    with open('ConversionResults.txt', 'w', encoding='utf-8') as file:
        file.write(table_str)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""Uso: python convertNumbers.py
              archivo_con_numeros1.txt [archivo_con_numeros2.txt ...]""")
    else:
        collected_conversions = process_files(sys.argv[1:])
        print_comparative_table(collected_conversions)
