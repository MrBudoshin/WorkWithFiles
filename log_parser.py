# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class LogParser:

    def __init__(self, file_name, against, last):
        self.file_name = file_name
        self.minute = {}
        self.count = against
        self.lasts = last

    def opening(self):

        with open(self.file_name, "r", encoding='cp1251') as file:
            for line in file:
                if "NOK" in line:
                    if line[self.count:self.lasts] in self.minute:
                        self.minute[line[self.count:self.lasts]] += 1
                    else:
                        self.minute[line[self.count:self.lasts]] = 1

    def saved(self, out_file_name=None):
        with open(out_file_name, 'w', encoding='utf8') as files:
            for time, date in self.minute.items():
                files.write('{}]: {}\n'.format(time, date))

    def run(self):
        self.opening()
        self.saved(out_file_name="parser.txt")


class Minute(LogParser):
    def __init__(self, file_name):
        super().__init__(file_name, against=0, last=17)


class Hour(LogParser):

    def __init__(self, file_name):
        super().__init__(file_name, against=0, last=14)


class Month(LogParser):

    def __init__(self, file_name):
        super().__init__(file_name, against=0, last=5)


minute = Minute(file_name="events.txt")
minute.run()
hour = Hour(file_name="events.txt")
hour.run()
month = Month(file_name="events.txt")
month.run()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!