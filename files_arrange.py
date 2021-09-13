# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)

class Arrange:

    def __init__(self, file_way, new_way):
        self.file_way = file_way
        self.new_way = new_way

    def file_walk(self):
        for address, dirs, files, in os.walk(self.file_way):
            for file_times in files:
                get_file_address = os.path.join(address, file_times)
                file_time = time.gmtime(os.path.getmtime(get_file_address))
                year_of_file = str(file_time[0])
                month_of_file = str(file_time[1]).zfill(2)
                ways = self.new_way
                address_file = os.path.join(ways, year_of_file, month_of_file)
                os.makedirs(address_file, exist_ok=True)
                file_way = os.path.join(ways, year_of_file, month_of_file, file_times)
                shutil.copy2(get_file_address, file_way)

    def act(self):
        self.file_walk()


file = Arrange("icons", "icons_by_year")
file.act()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
