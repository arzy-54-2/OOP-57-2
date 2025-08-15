from my_package.module1 import add, add_2
from my_package.module2 import min

# from my_package import add, add_2, min

# print(add(2,6))


from colorama import Fore, Back, Style
print(Fore.LIGHTCYAN_EX + 'some red text')
print(Back.BLACK + 'and with a green background')
print(Style.BRIGHT + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')