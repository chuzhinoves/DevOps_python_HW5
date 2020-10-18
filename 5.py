"""
5. Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from  _4 import (
    PoliceCar, WorkCar, TownCar, SportCar
)


wc = WorkCar(39, "green", "VW")
print(wc.color)
wc.color = "yellow"
print(wc.color)
wc.show_speed()
wc.speed = 45
wc.show_speed()
print(wc.is_police)

pc = PoliceCar(39, "black", "BMW")
print(pc.color)
pc.color = "white"
print(pc.color)
pc.show_speed()
pc.speed = 80
pc.show_speed()
print(pc.is_police)

