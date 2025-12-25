from models import HDD, Computer, CompHDD

computers = [
    Computer(1, 'Игровой ПК'),
    Computer(2, 'Офисный ПК'),
    Computer(3, 'Сервер'),
]

hdds = [
    HDD(1, 'Seagate Barracuda', 2000, 1),
    HDD(2, 'WD Red', 220000, 3),
    HDD(3, 'Kingston SSD', 500, 2),
    HDD(4, 'ADATA SSD Ultimate SU630', 240, 1),
    HDD(5, 'Samsung 970 Evo', 500, 3),
]

comps_hdds = [
    CompHDD(1, 1),
    CompHDD(1, 4),
    CompHDD(2, 3),
    CompHDD(3, 2),
    CompHDD(3, 5),
    CompHDD(3, 1),
    CompHDD(1, 3),
]
