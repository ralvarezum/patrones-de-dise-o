from creator import Creator
from concrete_creators import ConcreteCreatorA, ConcreteCreatorB

def client_code(creator):
    print(creator.operation())

if __name__ == "__main__":
    creator_a = ConcreteCreatorA()
    creator_b = ConcreteCreatorB()

    client_code(creator_a)
    client_code(creator_b)
