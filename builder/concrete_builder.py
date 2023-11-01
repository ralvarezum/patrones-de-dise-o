from product import Product
from builder import Builder

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self):
        self.product.part1 = "Parte 1 construida"

    def build_part2(self):
        self.product.part2 = "Parte 2 construida"

    def get_product(self):
        return self.product
