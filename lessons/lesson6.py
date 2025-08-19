class Test:


    def __init__(self):
        pass

    # def __str__(self):
    #     return "STR my"



# test = Test()
# print("Hello")
# print(test)


class Vector:


    def __new__(cls, *args, **kwargs):
        print("Hello")


    def __init__(self, array):
        self.array = array


    # def __add__(self, other):
    #     print(self.x)
    #     print(other.x)
    #     print("=====")
    #     print(self.y)
    #     print(other.y)
    #
    # def __eq__(self, other):
    #     if self.x == other.x:
    #         return print(True)
    #     else:
    #         return print(False)
    #
    # #     <
    # def __lt__(self, other):
    #     pass
    # #     >
    # def __gt__(self, other):
    #     pass

    def __setitem__(self, key, value):
        self.array[key] = value

    def __del__(self):
        print("Hello")

# obj_1 = Vector([4,5,6])
# obj_2 = Vector([1,2,3])
# obj_3 = obj_2 == obj_1

# print(obj_1.array)
# obj_1.array[1] = 99
# print(obj_1.array)


array_1 = [1,2,3,4,5,6,7,8,9,10,11]

def find_item(array, target):

    for i in array:
        if target == i:
            print('Найдет')

find_item(array_1, 543)

def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        print(f"left: {left} right: {right}")
        print(f"{left + right} ======" )
        print(f"{(left + right) // 2} =====")
        mid = (left + right) // 2
        if array[mid] == target:
            return print('Найден!!')
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return print("Не найден!!!")

binary_search(array_1, 1)





# # print(obj_1.array)
# print(array_1)
# # print(array_1[2])
# array_1[2] = 99
# print(array_1)

