from singleton import Singleton

singleton1 = Singleton()
singleton1.add_data("Dato 1")

singleton2 = Singleton()
singleton2.add_data("Dato 2")

print(singleton1.get_data())
print(singleton2.get_data())