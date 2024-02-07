"""
wordCount.py

Módulo diseñado para contar la frecuencia de cada palabra en un archivo de texto.
Los resultados se imprimirán en pantalla y se guardarán en un archivo llamado WordCountResults.txt.
Este script maneja errores adecuadamente, continúa su ejecución sin interrupciones,
y registra el tiempo total de ejecución.

Autor: Fernando Maytorena
"""

import sys
import time
from collections import Counter
from tabulate import tabulate

def read_words(file_path):
    """
    Lee todas las palabras de un archivo, ignorando los caracteres no alfabéticos.

    :param file_path: Ruta al archivo de texto a procesar.
    :return: Lista de palabras en el archivo.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().lower().split()
        words = [word.strip(".,!?;:'\"()[]{}") for word in words]
        return words
    except FileNotFoundError as e:
        print(f"Error al leer el archivo: {e}")
        return []

def count_words(words):
    """
    Cuenta la frecuencia de cada palabra única en la lista proporcionada.

    :param words: Lista de palabras a contar.
    :return: Un objeto Counter con la frecuencia de cada palabra.
    """
    return Counter(words)

def print_comparative_table(all_word_counts):
    """
    Imprime una tabla comparativa de los conteos de palabras para todos los archivos procesados.
    
    :param all_word_counts: Diccionario con la ruta del archivo como clave
    y su Counter de palabras como valor.
    """
    headers = ["Palabra"]
    headers.extend(all_word_counts.keys())
    table = []
    words = set()
    for word_counts in all_word_counts.values():
        words.update(word_counts.keys())

    for word in sorted(words):
        row = [word]
        for file_path in all_word_counts:
            row.append(all_word_counts[file_path].get(word, 0))
        table.append(row)

    table_str = tabulate(table, headers=headers, tablefmt="pretty")
    print(table_str)

    with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
        file.write(table_str)

def main(file_paths):
    """
    Función principal que procesa múltiples archivos de texto para contar la
    frecuencia de cada palabra.
    
    :param file_paths: Lista de rutas de archivos de texto a procesar.
    """
    all_word_counts = {}
    for file_path in file_paths:
        print(f"\nProcesando: {file_path}")
        start_time = time.time()
        words = read_words(file_path)
        word_counts = count_words(words)
        all_word_counts[file_path] = word_counts
        elapsed_time = time.time() - start_time
        print(f"Tiempo transcurrido para {file_path}: {elapsed_time:.4f} segundos")

    print_comparative_table(all_word_counts)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python wordCount.py archivo1.txt [archivo2.txt ...]")
    else:
        main(sys.argv[1:])
