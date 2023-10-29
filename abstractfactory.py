from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Operación A1"

class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Operación A2"

class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Operación B1"

class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Operación B2"

def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_a.operation_a()} y {product_b.operation_b()}")

if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    factory2 = ConcreteFactory2()

    client_code(factory1)
    client_code(factory2)
