from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def operation(self):
        product = self.factory_method()
        return f"Operación en {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteProductA:
    def operation(self):
        return "Producto A"

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

class ConcreteProductB:
    def operation(self):
        return "Producto B"

def client_code(creator):
    print(creator.operation())

if __name__ == "__main__":
    creator_a = ConcreteCreatorA()
    creator_b = ConcreteCreatorB()

    client_code(creator_a)
    client_code(creator_b)
