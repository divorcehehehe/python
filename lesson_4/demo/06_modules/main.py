# main.py: точка входа, geometry.py лежит рядом в той же папке
import geometry
from geometry import rect_area


def main():
    print(geometry.circle_area(2))
    print(rect_area(3, 4))
    print(geometry.perimeter(3, 4))
    print('__name__ здесь:', __name__)
    print('__name__ модуля:', geometry.__name__)


if __name__ == '__main__':
    main()
