from concrete_builder import ConcreteBuilder
from director import Director

if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)

    director.construct()
    product = builder.get_product()

    print(product)
