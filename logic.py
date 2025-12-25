from operator import itemgetter


def get_one_to_many(computers, hdds):
    """Связь один-ко-многим"""
    return [
        (h.name, h.capacity_gb, c.name)
        for c in computers
        for h in hdds
        if h.computer_id == c.id
    ]


def get_many_to_many(computers, hdds, comps_hdds):
    """Связь многие-ко-многим"""
    temp = [
        (c.name, ch.hdd_id)
        for c in computers
        for ch in comps_hdds
        if c.id == ch.computer_id
    ]

    return [
        (h.name, h.capacity_gb, c_name)
        for c_name, h_id in temp
        for h in hdds
        if h.id == h_id
    ]


# ===== Задание B1 =====
def query_b1(one_to_many):
    return [i for i in one_to_many if i[0].startswith('A')]


# ===== Задание B2 =====
def query_b2(one_to_many, computers):
    result = []

    for c in computers:
        c_hdds = list(filter(lambda i: i[2] == c.name, one_to_many))
        if c_hdds:
            min_capacity = min(map(lambda i: i[1], c_hdds))
            result.append((c.name, min_capacity))

    return sorted(result, key=lambda i: i[1])


# ===== Задание B3 =====
def query_b3(many_to_many):
    return sorted(many_to_many, key=itemgetter(0))


# ===== Запрос B2 =====
def query_b2(one_to_many, computers):
    result = []
    for c in computers:
        c_hdds = list(filter(lambda i: i[2] == c.name, one_to_many))
        if c_hdds:
            min_capacity = min(map(lambda i: i[1], c_hdds))
            result.append((c.name, min_capacity))
    return sorted(result, key=lambda i: i[1])


# ===== Запрос B3 =====
def query_b3(many_to_many):
    return sorted(many_to_many, key=itemgetter(0))
