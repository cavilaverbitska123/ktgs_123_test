# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
a = 'hello' # строка
a = [1, 1.0, 'hello'] # список
a = (1,1/0,'hello') # кортеж
a = {1,1.0,'hello'} #множество
a = frozenset ({1,1.0, 'hello'}) # неизменяемоее множество
a = {'a': 1, 'b':2} # словарь
a = b'hello' # байтовый тип
a = bytearray(b'hello')

a = [1, 1.0, 'hello'] # создаем список
help(a) # выводим информацию об 'a'
print(a) # выводим значение 'a'в консоль выводится сообщение и ожидается когда пользователь введет число
len(a) # сколько объектов в 'a'
min(a) #минимальное значение в 'a'
max(a) # максимальное значение в 'a'
type(a) # тип объекта 'a'