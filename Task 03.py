# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.

# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
#   только если введено число.
#  Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
#  При этом работа скрипта не должна завершаться.

class ListExcept:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = input('Press stop to exit. Enter values separated by space and finish by enter >>> ')
                if val == 'stop' or 'Stop':
                    print(f'Exit completed')
                    print(f'Final list >>> {self.my_list} \n ')
                    break
                else:
                    self.my_list.append(val)
                    print(f'Current list >>> {self.my_list} \n ')
            except:
                print(f"Wrong type! List for int and str only")
                again = input(f'Press Y to try again or anything else to exit. ')

                if again == 'Y' or again == 'y':
                    print(try_except.my_input())
                else:
                    return f'Exit completed'

try_except = ListExcept(1)
print(try_except.my_input())