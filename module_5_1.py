class House():
    def __init__(self, name, namber_of_floors):
        self.name = name
        self.namber_of_floors = int(namber_of_floors)
    def go_to(self,new_floor):
        self.new_floor = int(new_floor)
        print('Количество этажей -', new_floor)



new_floor = 10

h1 = House('ЖК Горский', 18)
print(h1.name, h1.namber_of_floors)
h1.go_to(5)
h2 = House('Домик в деревне', 2)
print(h2.name, h2.namber_of_floors)
h2.go_to(15)

#new_floor.go_to(5)
