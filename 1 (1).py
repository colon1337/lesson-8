#Написать класс “animals” (животные), который включает общие признаки и поведения животных. 
#От “animals” наследовать класс “mammals” (млекопитающие), который включает общие признаки и поведения млекопитающих. 
#От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака), у каждого свои признаки и поведения.
class Animals:
    def __init__(self, gender, name, age, weight, behavior):
        self.gender = gender
        self.name = name
        self.age = age
        self.weight = weight
        self.behavior = behavior
    
class Mammals(Animals):
    def __init__(self, gender, name, age, weight, behavior, behavior_mammals):
        super().__init__(gender, name, age, weight, behavior)
        self.behavior_mammals = behavior_mammals
        
class Human(Mammals):
    def __init__(self, gender, name, age, weight, behavior, behavior_mammals, speek):
        super().__init__(gender, name, age, weight, behavior, behavior_mammals)
        self.speek = speek
        
    def info(self):
        print(f'Имя:{self.name} Пол:{self.gender} Возраст:{self.age} Вес:{self.weight} Поведение:{self.behavior} Поведение:{self.behavior} Что делает сейчас:{self.behavior_mammals} Говорит:{self.speek}')
        
class Cat(Mammals):
    def __init__(self, gender, name, age, weight, behavior, behavior_mammals, meows):
        super().__init__(gender, name, age, weight, behavior, behavior_mammals)
        self.meows = meows
        
    def info(self):
        print(f'Имя:{self.name} Пол:{self.gender} Возраст:{self.age} Вес:{self.weight} Поведение:{self.behavior} Поведение:{self.behavior} Что делает сейчас:{self.behavior_mammals} Мяукает:{self.meows}')
        
class Dog(Mammals):
    def __init__(self, gender, name, age, weight, behavior, behavior_mammals, barking):
        super().__init__(gender, name, age, weight, behavior, behavior_mammals)
        self.barking = barking
    
    def info(self):
        print(f'Имя:{self.name} Пол:{self.gender} Возраст:{self.age} Вес:{self.weight} Поведение:{self.behavior} Поведение:{self.behavior} Что делает сейчас:{self.behavior_mammals} Гавкает:{self.barking}')
    
Sam = Human('м', 'Сэм', 25, 85, 'стоит/лежит/бегает/сидит', 'стоит', 'да')
Chuppy = Dog('м', 'Чаппи', 2, 20, 'стоит/лежит/бегает/сидит', 'бежит', 'да')
Murka = Cat('ж', 'Мурка', 10, 15, 'стоит/лежит/бегает/сидит', 'сидит', 'да')
Sam.info()
Chuppy.info()
Murka.info()


