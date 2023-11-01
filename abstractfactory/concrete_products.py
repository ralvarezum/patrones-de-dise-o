from abstract_products import AbstractProductA, AbstractProductB

class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Operación A1"

class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Operación A2"

class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Operación B1"

class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Operación B2"
