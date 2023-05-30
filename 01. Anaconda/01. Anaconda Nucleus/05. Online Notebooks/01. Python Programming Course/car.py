class Car:
    
    def __init__(self, brand, model, year, num_doors, owner, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.num_doors = num_doors
        self.owner = owner
        self.mileage = mileage
        
    def describe_car(self):
        print(f"It is a {self.brand} {self.model} from {self.year}. It has {self.num_doors} doors "
              f"and its' owner is {self.owner}. Its' mileage is {self.mileage} km.")
        
    def newest_mileage(self, mileage_increase = 5000):
        self.mileage += mileage_increase
        print(f'{self.owner} drove {mileage_increase} since the last check. '
              f'Current mileage is {self.mileage}.')