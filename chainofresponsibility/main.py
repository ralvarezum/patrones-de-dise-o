from handler import ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC

if __name__ == "__main__":
    handlerA = ConcreteHandlerA()
    handlerB = ConcreteHandlerB()
    handlerC = ConcreteHandlerC()

    handlerA.successor = handlerB
    handlerB.successor = handlerC

    requests = ["A", "B", "C", "D"]

    for request in requests:
        handlerA.handle_request(request)
