# 1. Декоратор @staticmethod
# Декоратор @staticmethod используется для того, чтобы определить метод, который не зависит от экземпляра класса
# (не использует self) и не зависит от самого класса (не использует cls). Такой метод можно вызывать без создания
# экземпляра класса.

class Math:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def add(a, b):
        return a + b

    def get_name(self):
        return self.name

# print(Math.add(2,7))

# my_obj = Math("name")
# print(my_obj.get_name())


# 2. Декоратор @classmethod
# Описание:
# Декоратор @classmethod используется для определения метода, который принимает первым аргументом
# сам класс (не экземпляр). Этот аргумент обычно называется cls. Метод класса может изменять состояние класса,
#  но не работает с состоянием конкретного экземпляра.


# class Person:
#
#     # Атрибута класса
#     population = 0
#
#     def __init__(self, name):
#         # Атрибута объекта класса
#         self.name = name
#         Person.population += 1
#
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
#     @classmethod
#     def create_person(cls, name):
#         return cls(name)

# obj_1 = Person.create_person("Name1")
# obj_2 = Person("Name2")

# print(Person.get_population())


# 3. Декоратор @property
# Описание:
# Декоратор @property используется для того, чтобы метод стал доступным как атрибут, но при этом оставался методом.
# Это позволяет скрывать логику вычислений или проверки, делая код более чистым. Обычно используется
# для создания геттеров и сеттеров.

class Circle:

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):
        return 3.14 * self.__radius ** 2


circle = Circle("123")

# print(circle.radius)



class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

ardager = User("Ardager", "Kartanbekov")

# print(f"full name: {ardager.first_name} {ardager.last_name}")
# print(f"full name: {ardager.full_name}")


# 1. Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в дополнительную функциональность.

def simple_decorator(func):
    def wrapper():
        print("До выполнения любая логика")
        func()
        print("После выполнения любая логика")
    return wrapper


@simple_decorator
def say_hello():
    print('Hello world!!')

# say_hello()

def greeting_decorator(func):
    def wrapper(name_wrap):
        print(f"Привет {name_wrap}")
        func(name_wrap)
    return wrapper

@greeting_decorator
def greeting(name):
    print(f"Как дела {name} ?")

# greeting("Ardager")


def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat_decorator(5)
def hello():
    print("Hello!!")

# hello()

def class_decorator(cls):
    class NewClass(cls):

        @staticmethod
        def new_method():
            return "new method"
    return NewClass

@class_decorator
class OldClass:
    @staticmethod
    def old_method():
        return "old method"

obj_1 = OldClass

print(obj_1.old_method())