from abc import ABC, abstractmethod

# Interfaz Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# Fábrica concreta 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

# Fábrica concreta 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

# Interfaz Abstract Product A
class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

# Clase concreta de producto A1
class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Operación A1"

# Clase concreta de producto A2
class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Operación A2"

# Interfaz Abstract Product B
class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

# Clase concreta de producto B1
class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Operación B1"

# Clase concreta de producto B2
class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Operación B2"

# Función para realizar operaciones con una fábrica concreta
def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_a.operation_a()} y {product_b.operation_b()}")

if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    factory2 = ConcreteFactory2()

    client_code(factory1)  # Salida: Operación A1 y Operación B1
    client_code(factory2)  # Salida: Operación A2 y Operación B2
