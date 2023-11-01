from abstract_factory import AbstractFactory
from concrete_factories import ConcreteFactory1, ConcreteFactory2

def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_a.operation_a()} y {product_b.operation_b()}")

if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    factory2 = ConcreteFactory2()

    client_code(factory1)
    client_code(factory2)
