# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
#   корректно обработать эту ситуацию и не завершиться с ошибкой.

class NullDivClass:
    def __init__(self, divisible, divider):
        self.divider = divisible
        self.denominator = divider

    @staticmethod
    def divide_by_null(divisible, divider):
        try:
            return (divisible / divider)
        except:
            return (f"No division by zero!")

print(NullDivClass.divide_by_null(13, 0))
print(NullDivClass.divide_by_null(24, 2))
print(NullDivClass.divide_by_null(42, 0.1))