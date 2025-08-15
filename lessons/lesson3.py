# Инкапсуляция
# # Когда имя атрибута или метода начинается с одного подчеркивания (например, _balance),
# # это обозначает, что он защищен
# # или может начитаться с двух подчеркиваний (__balance), что обозначает, что он приват

import random

class BankAccount:

    def __init__(self, customer, balance, password):
        self.customer = customer
        self._balance = balance
        self.__password = password


    def __random_password(self):
        return random.randint(1, 6)

    def login(self, password):
        if self.__password == password:
            print('Вы вошли!!')
        else:
            print("не верный пароль!!!")

    def get_balance(self):
        return print(self._balance)

    def get_random_password(self):
        return self.__random_password()

account_1 = BankAccount("John Doe", 10000, 123)

# print(account_1._BankAccount__random_password())


# # Абстракция позволяет сосредоточиться на общих характеристиках, скрывая детали
# # реализации. Это можно сделать, создавая абстрактные классы, которые определяют
# # интерфейс (методы) для классов-наследников. В Python абстрактные классы обычно
# # создаются с помощью модуля abc.

from abc import ABC, abstractmethod


class Animals(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


# class Dog(Animal):
#
#     def make_sound(self):
#         print('Gaf gaf')
#
#     def move(self):
#         print('step step')
#
# class Fish(Animal):
#
#     def make_sound(self):
#         print('bul bul ')
#
#     def move(self):
#         print('swimming')

# dog = Dog()
# fish = Fish()
#
# fish.move()
# dog.move()

class AbcOtpSender(ABC):

    @abstractmethod
    def send_sms_to_phone(self):
        pass


class KgSenderSms(AbcOtpSender):

    def send_sms_to_phone(self):
        pass




class Swimm:
    def move(self):
        return print('Плавает')

class Flyable:
    def move(self):
        return print('Летит!!')


class Animal:
    def make_sound(self):
        return print('Издает звук')

    def move(self):
        return print('Двигается')

class Duck(Swimm, Flyable, Animal):
    def make_sound(self):
        return print('Кря Кря')

# donald_duck = Duck()
#
# # donald_duck.move()
# print(Duck.__mro__)



class A:
    def action(self):
        return print('A')


class B(A):
    def action(self):
        super().action()
        return print('B')


class C(A):
    def action(self):
        super().action()
        return print('C')

class D(B, C):
    pass
    # def action(self):
    #     return print('D')
d = D()
d.action()

# print(D.__mro__)



# ===========

from lesson1 import Hero

test = Hero("Kirito", 100, 100)