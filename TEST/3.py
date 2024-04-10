"""
3. Создать класс Point, который представляет собой точку в двумерном пространстве.
Класс должен иметь методы для инициализации координат точки,
вычисления расстояния до другой точки, а также для получения и изменения координат.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


x1 = int(input('x: '))
y1 = int(input('y: '))

x2 = int(input('x: '))
y2 = int(input('y: '))

p = Point(x1, y1)
q = Point(x2, y2)

print(p.distance_to(q))
print(f'Координаты точки p: {p.get_coordinates()}')
p.set_coordinates(3, 6)
print(p.get_coordinates())
