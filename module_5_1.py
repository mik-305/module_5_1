class House():
    def __init__(self, name, namber_of_floors):
        self.name = name
        self.namber_of_floors = int(namber_of_floors)
    def go_to(self,new_floor):
        for i in range(new_floor):
            if new_floor <= self.namber_of_floors:
                print('Номер этажа ', i+1)
            else:
                print('Такого этажа не существует!')
                break


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

