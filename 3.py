"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

import unittest

range_income = {
    "stager" : {"wage": 0, "bonus" : 0},
    "junior" : {"wage": 50, "bonus" : 50}, 
    "middle" : {"wage": 70, "bonus" : 70},
    "senior" : {"wage": 90, "bonus" : 90},
    "lead" : {"wage": 120, "bonus" : 120},
    "pr. manager" : {"wage": 150, "bonus" : 150},
    "pr. director" : {"wage": 200, "bonus" : 300}
}

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = range_income[position]

class Position(Worker):
    
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


class test_Position(unittest.TestCase):
    def test_get_full_name(self):
        pos = Position("Иван", "Иванов", "junior")
        self.assertEqual(pos.get_full_name(), "Иван Иванов")
    
    def test_get_total_income(self):
        pos = Position("Иван", "Иванов", "junior")
        self.assertEqual(pos.get_total_income(), 100)
        

if __name__ == "__main__":
    unittest.main()