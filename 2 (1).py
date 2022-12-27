#Написать класс “Student”, который наследует класс human, у которого среди прочих признаков есть “Количество сданных дз”
class Human:
    def __init__(self, gender, name, age, weight, quantities_of_homework):
        self.gender = gender
        self.name = name
        self.age = age
        self.weight = weight
        self.quantities_of_homework = quantities_of_homework
        
class Student(Human):
    def __init__(self, gender, name, age, weight, quantities_of_homework):
        super().__init__(gender, name, age, weight, quantities_of_homework)
    
    def homework(self):
        print(f'Имя:{self.name} Пол:{self.gender} Возраст:{self.age} Вес:{self.weight} Количество сделанных дз:{self.quantities_of_homework}')

Student1 = Student('m', 'pasha', 3, 41, 5)
Student2 = Student('m', 'misha', 3, 41, 6)
Student3 = Student('m', 'sasha', 3, 41, 5)
Student2.homework()



