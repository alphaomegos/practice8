# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, strdate):
        '''
        Дата вводится в виде строки, где день месяц и год разделены пробелами
        '''
        self.strdate = str(strdate)

    @classmethod
    def extract(cls, strdate):
        my_date = []

        for i in strdate.split():
            if i != '': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Correct date\n'
                else:
                    return f'Wrong year! Year should be between 0 and 2021\n'
            else:
                return f'Wrong month! Month should be between 1 and 12!\n'
        else:
            return f'Wrong day! Day should be between 1 and 31\n'

    def __str__(self):
        return f'Current date >>>  {Data.extract(self.strdate)}\n'


today = Data('11 1 2001')
userdate = str(input('Enter date in format DD MM YYYY divided by spaces >>> '))
Uday = int(input('Enter day >>> '))
Umonth = int(input('Enter month >>> '))
Uyear = int(input('Enter year >>> '))
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract(userdate))
print(today.extract('11 11 2020'))
print(Data.valid(Uday, Umonth, Uyear))