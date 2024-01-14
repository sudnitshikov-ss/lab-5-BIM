import doctest

class Table:
    def __init__(self, lines: int, columns: int):
        self.attr1 = lines
        self.attr2 = columns
        if not isinstance(self.attr1, (int, float)):
            raise TypeError("Число строк должно быть типа int или float")
        if not isinstance(self.attr2, (int, float)):
            raise TypeError("Число столбцов должно быть типа int или float")
        if lines <= 0:
            raise ValueError("Число строк должно быть положительным числом")
        if columns <= 0:
            raise ValueError("Число столбцов должно быть положительным числом")

    def method_1(self):
        ...

    def method_2(self):
        ...

    def method_3(self):
        ...

class Tree:
    def __init__(self, height: float, diameter_of_trunk: float):
        self.attr1 = height
        self.attr2 = diameter_of_trunk

    def method_1(self):
        ...

    def method_2(self):
        ...

    def method_3(self):
        ...

class Bookshelf:
    def __init__(self, number_of_shelves: int, height: float):
        self.attr1 = number_of_shelves
        self.attr2 = height

    def method_1(self):
        ...

    def method_2(self):
        ...

    def method_3(self):
        ...

if __name__ == "__main__":
    doctest.testmod()