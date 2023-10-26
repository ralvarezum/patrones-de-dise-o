from abc import ABC, abstractmethod

# Interfaz para la creación de productos
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def operation(self):
        product = self.factory_method()
        return f"Operación en {product.operation()}"

# Clase concreta que implementa la creación de productos
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

# Clase concreta de producto
class ConcreteProductA:
    def operation(self):
        return "Producto A"

# Otra clase concreta que implementa la creación de productos
class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Otra clase concreta de producto
class ConcreteProductB:
    def operation(self):
        return "Producto B"

# Función para realizar la operación
def client_code(creator):
    print(creator.operation())

if __name__ == "__main__":
    creator_a = ConcreteCreatorA()
    creator_b = ConcreteCreatorB()

    client_code(creator_a)  # Salida: Operación en Producto A
    client_code(creator_b)  # Salida: Operación en Producto B
