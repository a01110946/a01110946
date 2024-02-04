"""
computeStatistics.py

Módulo para calcular estadísticas descriptivas de datos en un archivo.

Autor: Fernando Maytorena"""

import sys
import time
from tabulate import tabulate

def read_data(file_path):
    """Lee datos numéricos de un archivo y devuelve una lista de flotantes."""
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    data.append(float(line.strip()))
                except ValueError:
                    print(f"""Error: No se pudo convertir a flotante:
                          '{line.strip()}'. Se salta línea.""")
        return data
    except FileNotFoundError as e:
        print(f"Error al leer el archivo: {e}")
        return []

def calculate_statistics(data):
    """
    Calcula las estadísticas descriptivas de una lista de números y las retorna en un diccionario.
    
    :param data: Lista de números (flotantes o enteros).
    :return: Diccionario con la media, mediana, moda, varianza y desviación estándar.
    """
    if not data:
        return None
    data.sort()
    stats = {
        'n': len(data),
        'mean': sum(data) / len(data),
        'median': data[len(data) // 2] if len(data) % 2 != 0 else (data[len(data) // 2 - 1]
                                                                   + data[len(data) // 2]) / 2,
        'mode': max(set(data), key=data.count),
        'variance': sum((x - sum(data) / len(data)) ** 2 for x in data) / len(data),
        'std_dev': (sum((x - sum(data) / len(data)) ** 2 for x in data) / len(data)) ** 0.5
    }
    return stats

def create_results_str(results, elapsed_time):
    """
    Crea una cadena de texto con las estadísticas descriptivas y el tiempo transcurrido.
    
    :param results: Una tupla con estadísticas descriptivas calculadas.
    :param elapsed_time: Tiempo transcurrido durante la ejecución y cálculos.
    :return: String formateado con los resultados.
    """
    return f"""Estadísticas Descriptivas:
Conteo: {results['n']}
Media: {results['mean']}
Mediana: {results['median']}
Moda: {results['mode']}
Deviación Estándar: {results['std_dev']}
Variancia: {results['variance']}
Tiempo transcurrido: {elapsed_time:.4f} segundos
"""

def print_and_save_results(results, elapsed_time, file_name='StatisticsResults.txt'):
    """
    Genera y guarda una cadena de texto con las estadísticas descriptivas
    y el tiempo transcurrido en un archivo.
    
    Utiliza los resultados calculados almacenados en un diccionario
    y el tiempo transcurrido para crear una cadena de texto
    formatada con las estadísticas descriptivas, que luego imprime
    y guarda en el archivo especificado.
    
    :param results: Diccionario con estadísticas descriptivas calculadas
    (contiene n, mean, median, mode, variance, std_dev).
    :param elapsed_time: Tiempo transcurrido durante la ejecución y cálculos, en segundos.
    :param file_name: Nombre del archivo para guardar resultados.
    Predeterminado a 'StatisticsResults.txt'.
    """
    results_str = create_results_str(results, elapsed_time)
    print(results_str)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(results_str)

def main(file_paths):
    """
    Función principal que procesa múltiples archivos de datos, 
    calcula estadísticas y las imprime en una tabla comparativa.
    
    :param file_paths: Lista de rutas de archivos de datos a procesar.
    """
    all_results = []
    for file_path in file_paths:
        start_time = time.time()
        data = read_data(file_path)
        if not data:
            print(f"""No se pudieron leer datos de {file_path}.
                  Continuando con el siguiente archivo.""")
            continue
        results = calculate_statistics(data)
        elapsed_time = time.time() - start_time
        all_results.append((file_path, results, elapsed_time))

    with open('StatisticsResults.txt', 'w', encoding='utf-8') as file:
        for file_path, results, elapsed_time in all_results:
            if results is not None:
                results_str = create_results_str(results, elapsed_time)
                print(f"Archivo: {file_path}\n{results_str}")
                file.write(f"Archivo: {file_path}\n{results_str}\n")
            else:
                error_message = f"""Archivo: {file_path} - No se pueden calcular
                estadísticas sobre un archivo vacío.\n"""
                print(error_message)
                file.write(error_message)

    headers = ["Archivo", "Conteo", "Media", "Mediana", "Moda", "Deviación Estándar",
               "Variancia", "Tiempo Transcurrido"]
    table = []
    for file_path, results, elapsed_time in all_results:
        if results is not None:
            table.append([file_path, results['n'], f"{results['mean']:.2f}",
                          f"{results['median']:.2f}", results['mode'],
                        f"{results['std_dev']:.2f}", f"{results['variance']:.2f}",
                        f"{elapsed_time:.4f} s"])
        else:
            table.append([file_path, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A",
                          f"{elapsed_time:.4f} s"])

    print(tabulate(table, headers=headers, tablefmt="pretty"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py fileWithData1.txt [fileWithData2.txt ...]")
    else:
        main(sys.argv[1:])
