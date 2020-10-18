"""
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    
    def show_speed(self):
        print(self.speed)
    
    def go(self):
        print("Машина поехала")
    
    def stop(self):
        print("Машина остановилась")
    
    def turn(self, direction):
        print(f"Машина повернула {direction}")

class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if (self.speed > 60):
            print("превышение скорости")
        
class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if (self.speed > 40):
            print("превышение скорости")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = True
