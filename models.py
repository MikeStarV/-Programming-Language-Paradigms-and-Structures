class HDD:
    def __init__(self, id, name, capacity_gb, computer_id):
        self.id = id
        self.name = name
        self.capacity_gb = capacity_gb
        self.computer_id = computer_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CompHDD:
    def __init__(self, computer_id, hdd_id):
        self.computer_id = computer_id
        self.hdd_id = hdd_id
