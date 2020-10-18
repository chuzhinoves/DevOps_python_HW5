"""
6. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер)
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    tittle = "Unknow"
    
    def draw(self):
        pass


class Pen(Stationery):
    def __init__(self):
        self.tittle = "Pen"
    
    def draw(self):
        print("Pen line")
    
class Pencil(Stationery):
    def __init__(self):
        self.tittle = "Pencil"
    
    def draw(self):
        print("Pencil line")


class Handle(Stationery):
    def __init__(self):
        self.tittle = "Handle"
    
    def draw(self):
        print("Handle line")

pen, pencil, handle = Pen(), Pencil(), Handle()

pen.draw()
pencil.draw()
handle.draw()