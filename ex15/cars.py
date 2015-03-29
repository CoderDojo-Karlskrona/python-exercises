class Car:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

cars = list()
cars.append(Car("Saab", "95"))    
cars.append(Car("Volvo", "740"))
cars.append(Car("Ferrari", "458"))
cars.append(Car("Porsche", "911"))
cars.append(Car("Corvette", "Stingray"))

for car in cars:
    print car.mark + " " + car.model
