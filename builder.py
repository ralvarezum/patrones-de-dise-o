class Product:
    def __init__(self):
        self.part1 = None
        self.part2 = None

    def __str__(self):
        return f"Parte 1: {self.part1}, Parte 2: {self.part2}"

class Builder:
    def build_part1(self):
        pass

    def build_part2(self):
        pass

    def get_product(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self):
        self.product.part1 = "Parte 1 construida"

    def build_part2(self):
        self.product.part2 = "Parte 2 construida"

    def get_product(self):
        return self.product

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part1()
        self.builder.build_part2()

if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)

    director.construct()
    product = builder.get_product()

    print(product)
