from abc import ABC, abstractmethod

# Interfaz Subject (Sujeto)
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Clase ConcreteSubject (Sujeto concreto)
class ConcreteSubject(Subject):
    def __init__(self):
        self._state = None
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def set_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state

# Interfaz Observer (Observador)
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

# Clase ConcreteObserver (Observador concreto)
class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"El estado del sujeto ha cambiado a {subject.get_state()}")

if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.set_state("Estado 1")  # Notificará a los observadores

    subject.detach(observer2)  # Eliminar un observador

    subject.set_state("Estado 2")  # Solo notificará a observer1
