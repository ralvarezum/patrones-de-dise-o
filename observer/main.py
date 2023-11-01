from subject import ConcreteSubject
from observer import ConcreteObserver

if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.set_state("Estado 1")

    subject.detach(observer2)

    subject.set_state("Estado 2")
