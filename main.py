from operator import itemgetter

class HDD:
    """Жесткий диск"""

    def __init__(self, id, name, capacity_gb, computer_id):
        self.id = id
        self.name = name
        self.capacity_gb = capacity_gb
        self.computer_id = computer_id


class Computer:
    """Компьютер"""

    def __init__(self, id, name):
        self.id = id
        self.name = name

class CompHDD:
    """ 'Диски в Компьютерах' для реализации связи многие-ко-многим"""
    def __init__(self, computer_id, hdd_id):
        self.computer_id = computer_id
        self.hdd_id = hdd_id


#     Данные


computers = [
    Computer(1, 'Игровой ПК'),
    Computer(2, 'Офисный ПК'),
    Computer(3, 'Сервер'),
]

hdds = [
    HDD(1, 'Seagate Barracuda', 2000, 1),
    HDD(2, 'WD Red', 220000, 3),
    HDD(3, 'Kingston SSD', 500, 2),
    HDD(4, 'ADATA SSD Ultimate SU630', 240,  1),
    HDD(5, 'Samsung 970 Evo', 500, 3)
]


comps_hdds = [
    CompHDD(1, 1),  # Игровой ПК -> Seagate
    CompHDD(1, 4),  # Игровой ПК -> ADATA
    CompHDD(2, 3),  # Офисный ПК -> Kingston
    CompHDD(3, 2),  # Сервер -> WD Red (id 2)
    CompHDD(3, 5),  # Сервер -> Samsung

    # Дополнительные связи "многие-ко-многим"
    # Показываем, что диск (id 1) может быть в нескольких ПК
    CompHDD(3, 1),  # Сервер -> Seagate (id 1)
    # Показываем, что ПК (id 1) может иметь еще диски
    CompHDD(1, 3),  # Игровой ПК -> Kingston (id 3)
]


def main():
    """Основная функция"""
    # Соединение данных  (list comprehension использовал)

    # Соединение данных один-ко-многим (Компьютер -> Диски)
    one_to_many = [(h.name, h.capacity_gb, c.name)
                   for c in computers
                   for h in hdds
                   if h.computer_id == c.id]

    temp_many_to_many = [(c.name, ch.computer_id, ch.hdd_id)
                         for c in computers
                         for ch in comps_hdds
                         if c.id == ch.computer_id]

    many_to_many = [(h.name, h.capacity_gb, c_name)
                    for c_name, c_id, h_id in temp_many_to_many
                    for h in hdds if h.id == h_id]

    # Запросы Варианта В

    print('Задание B1')
    res_1 = [i for i in one_to_many if i[0].startswith('A')] #list comprehension для фильтрации
    print(res_1)

    print('\nЗадание B2')
    temp_res = []
    for c in computers:

        c_hdds = list(filter(lambda i: i[2] == c.name, one_to_many)) # Список дисков для текущего компьютера

        if len(c_hdds) > 0:
            c_capacities = list(map(lambda i: i[1] , c_hdds))
            min_cap = min(c_capacities)
            temp_res.append((c.name, min_cap))

    res_2 = sorted(temp_res, key=lambda i: i[1]) #использовал лямбду для разнообразия)
    print(res_2)

    print('\nЗадание B3')
    res_3 = sorted(many_to_many, key=itemgetter(0))
    print(res_3)


if __name__ == '__main__':
    main()





