class Person:
    
    def __init__(self, name, age, birthplace, city, function):
        self.name = name
        self.age = age
        self.birthplace = birthplace
        self.city = city
        self.function = function
    
    def introduce_yourself(self):
        print(f'Hello, my name is {self.name}. I am {self.age} years old. '
              f'I was born in {self.birthplace} and live now in {self.city}. '
              f'My function is {self.function}.')
        
    def age_person(self, incr_age = 1):
        self.age += incr_age
        print(f'{self.name} is now {self.age} years old.')

class Student(Person):
    
    def __init__(self, name, age, birthplace, city, function, university, graduated, gpa):
        super().__init__(name, age, birthplace, city, function)
        self.university = university
        self.graduated = graduated
        self.gpa = gpa