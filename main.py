from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square


def main():
    r = Rectangle("красного", 5, 2)
    c = Circle("красного", 7)
    s = Square("красного", 8)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()