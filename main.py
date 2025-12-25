from data import computers, hdds, comps_hdds
from logic import *

def main():
    one_to_many = get_one_to_many(computers, hdds)
    many_to_many = get_many_to_many(computers, hdds, comps_hdds)

    print("Задание B1")
    print(query_b1(one_to_many))

    print("\nЗадание B2")
    print(query_b2(one_to_many, computers))

    print("\nЗадание B3")
    print(query_b3(many_to_many))


if __name__ == '__main__':
    main()





