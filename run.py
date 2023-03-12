# Quebra do princípip de Liskov
# A herança deve ser uma complementação

class PersonA:
    
    def introduce_yourself(self):
        print('Hi! I am person A')

class PersonB(PersonA):
    def __init__(self):
        super().__init__()
        
    def introduce_yourself(self):
        print('I am changing this method')

person = PersonA()
person.introduce_yourself()

person2 = PersonB()
person2.introduce_yourself()