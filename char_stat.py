# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class Alphabet:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.alpha_quantit = []

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def sort_alphabet(self):
        for letter, frequency in sorted(self.stat.items()):
            self.alpha_quantit.append((letter, frequency))

    def printed(self):
        summa = sum(self.stat.values())
        print("+", "-" * 9, "+", "-" * 9, " +")
        print("| ", " Буква ", " | ", " Частота", " | ")
        print("+", "-" * 9, "+", "-" * 9, " +")
        for refresh in self.alpha_quantit:
            print('| {letter:^9} | {frequency:^10d} |'.format(letter=refresh[0], frequency=refresh[1]))
        print("+", "-" * 9, "+", "-" * 9, " +")
        print("| ", " Итого ", " | ", summa, "  |")
        print("+", "-" * 9, "+", "-" * 9, " +")

    def act(self):
        self.collect()
        self.sort_alphabet()
        self.printed()


class Lower(Alphabet):

    def __init__(self, file_name):
        super().__init__(file_name)

    def sort_alphabet(self):
        for letter, frequency in sorted(self.stat.items(), reverse=True):
            self.alpha_quantit.append((letter, frequency))


class Increase(Alphabet):

    def __init__(self, file_name):
        super().__init__(file_name)

    def sort_alphabet(self):
        list_a = list(self.stat.items())
        list_a.sort(key=lambda i: i[1])
        for i in list_a:
            self.alpha_quantit.append(i)


class Decrease(Alphabet):

    def __init__(self, file_name):
        super().__init__(file_name)

    def sort_alphabet(self):
        list_a = list(self.stat.items())
        list_a.sort(key=lambda i: i[1], reverse=True)
        for i in list_a:
            self.alpha_quantit.append(i)


upper = Alphabet(file_name='voyna-i-mir.txt.zip')
upper.act()
lower = Lower(file_name='voyna-i-mir.txt.zip')
lower.act()
increase = Increase(file_name='voyna-i-mir.txt.zip')
increase.act()
decrease = Decrease(file_name='voyna-i-mir.txt.zip')
decrease.act()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
#зачет!