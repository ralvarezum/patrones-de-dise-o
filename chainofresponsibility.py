class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("Manejado por ConcreteHandlerA")
        else:
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("Manejado por ConcreteHandlerB")
        else:
            super().handle_request(request)

class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == "C":
            print("Manejado por ConcreteHandlerC")
        else:
            print("No se pudo manejar la solicitud")

if __name__ == "__main__":
    handlerA = ConcreteHandlerA()
    handlerB = ConcreteHandlerB()
    handlerC = ConcreteHandlerC()

    handlerA.successor = handlerB
    handlerB.successor = handlerC

    requests = ["A", "B", "C", "D"]

    for request in requests:
        handlerA.handle_request(request)
