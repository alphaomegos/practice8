# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта,
#   создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
#   Проверьте корректность полученного результата.

class ComplexOperations:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Sum is equal')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Multiplication')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


First = ComplexOperations(5, -2)
Second = ComplexOperations(2, 4)
print(First)
print(First + Second)
print(First * Second)