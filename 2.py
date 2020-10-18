"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""

import unittest

class Road:
    
    MASS_FOR_ONE = 25
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def mass(self, tickness):
        return (self.length * self.width * 
                self.MASS_FOR_ONE * tickness) / 1000

class tesing_Road(unittest.TestCase):
    def test_mass(self):
        length = 5000
        width = 20
        tickness = 5
        road = Road(length, width)
        self.assertEqual(road.mass(tickness), 12500)

if __name__ == "__main__":
    unittest.main()