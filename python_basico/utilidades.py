# -*- coding: utf-8 -*-
"""Módulo de ejemplo usado por 05_modulos_y_archivos.ipynb para mostrar
un import local (propio del proyecto), además de los imports de la
librería estándar."""


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte una temperatura de Celsius a Fahrenheit."""
    return celsius * 9 / 5 + 32


def es_primo(n: int) -> bool:
    """Determina si `n` es un número primo."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True
