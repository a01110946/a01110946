"""
computeSales.py

Este módulo implementa la funcionalidad para calcular el total de ventas basado
en archivos JSON de catálogo de precios y registros de ventas. Alineado con
PEP-8 y con manejo de errores básico.

Autor: Fernando Maytorena
Fecha: 2021-09-26

Uso: python computeSales.py priceCatalogue.json salesRecord.json
"""

import sys
import json
import time


def load_json(file_path):
    """Carga y devuelve el contenido de un archivo JSON dado su ruta."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def calculate_total_sales(prices, sales):
    """
    Calcula el total de ventas multiplicando el precio de cada producto
    por su cantidad vendida.
    :param prices: Diccionario con los precios de los productos.
    :param sales: Lista de diccionarios, cada uno representando una venta.
    :return: El costo total de las ventas.
    """
    total_cost = 0
    for sale in sales:
        product_title = sale.get('Product')
        product_price = next((item['price'] for item in prices
                              if item['title'] == product_title), None)
        if product_price is None:
            print(f"Producto no encontrado o ID inválido: {product_title}")
            continue
        quantity = sale.get('Quantity', 0)
        total_cost += product_price * quantity
    return total_cost


def main(price_catalogue_path, sales_record_path):
    """
    Función principal que carga los datos, calcula el total de ventas,
    e imprime y guarda los resultados.
    :param price_catalogue_path: Ruta al archivo JSON del catálogo de precios.
    :param sales_record_path: Ruta al archivo JSON del registro de ventas.
    """
    start_time = time.time()
    prices = load_json(price_catalogue_path)
    sales = load_json(sales_record_path)
    total_cost = calculate_total_sales(prices, sales)
    elapsed_time = time.time() - start_time
    results_str = f"""Costo total de ventas: {total_cost}\n
    Tiempo transcurrido: {elapsed_time:.2f} segundos\n"""
    print(results_str)
    return results_str


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) % 2 != 0 or len(args) == 0:
        print("Uso: python computeSales.py priceCatalogue1.json salesRecord1.json [...]")
    else:
        # Asegurarse de que el archivo SalesResults.txt esté vacío al inicio
        open('SalesResults.txt', 'w', encoding='utf-8').close()

        for i in range(0, len(args), 2):
            processing_str = f"{args[i]} y {args[i + 1]}"
            print(processing_str)
            result_str = main(args[i], args[i + 1])
            with open('SalesResults.txt', 'a', encoding='utf-8') as output_file:
                output_file.write(processing_str + "\n" + result_str + "\n\n----------\n\n")
