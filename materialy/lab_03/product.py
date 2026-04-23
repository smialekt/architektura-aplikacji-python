# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError('Product amount cannot be lower than 0')

        self.quantity += amount
        pass

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError('Product amount cannot be lower than 0')
        if amount > self.quantity:
            raise ValueError('Product amount cannot be lower than 0')

        self.quantity -= amount

    def is_available(self) -> bool:
        return True if self.quantity > 0 else False

    def total_value(self) -> float:
        return self.price * self.quantity
