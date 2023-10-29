class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_data()
        return cls._instance

    def init_data(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def get_data(self):
        return self.data

singleton1 = Singleton()
singleton1.add_data("Dato 1")

singleton2 = Singleton()
singleton2.add_data("Dato 2")

print(singleton1.get_data())
print(singleton2.get_data())
