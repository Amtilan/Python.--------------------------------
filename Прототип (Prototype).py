# Тут рассмотрен пример порождающего шаблона проектирования программ «Прототип», 
# который позволяет копировать объекты, не вдаваясь в подробности их реализации. 
# Преимуществом паттерна является то, что он позволяет клонировать объекты, не привязываясь к их конкретным классам, 
# уменьшает повторяющийся код при инициализации объектов. Однако составные объекты, имеющие ссылки на другие классы, клонировать сложнее.

import copy

class Sheep:
    
    __name: str=''
    __params: dict={
        'Weight':20,
        'Height':34,
    }
    
    def __init__(self, donor: 'Sheep' = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())

    def set_name(self, name) -> None:
        self.__name=name
    
    def get_name(self) -> str:
        return self.__name
    
    def get_params(self) -> dict:
        return self.__params
    
    def set_weight(self, weight: int) -> None:
        self.__params['Weight']=weight

    def clone(self) -> 'Sheep':
        return Sheep(self)
    
def main() -> None:
    sheep_donor: Sheep=Sheep()
    sheep_donor.set_name('Barashek')
    
    sheep_clone: Sheep=sheep_donor.clone()
    
    print('Origin Sheep: ', sheep_donor.get_name(), sheep_donor.get_params())
    print('Cloned Sheep: ', sheep_clone.get_name(), sheep_clone.get_params())
    
    sheep_clone.set_name('Ne_Barashek')
    
    print('\nOrigin Sheep: ', sheep_donor.get_name(), sheep_donor.get_params())
    print('Cloned Sheep: ', sheep_clone.get_name(), sheep_clone.get_params())


if __name__ == "__main__":
    main()