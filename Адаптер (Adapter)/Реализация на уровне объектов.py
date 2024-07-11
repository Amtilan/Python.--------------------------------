# Тут рассмотрен пример структурного шаблона проектирования программ «Адаптер», 
# предназначенный для организации использования функций объекта, недоступного для модификации,
# через специально созданный интерфейс. Другими словами, он позволяет объектам с несовместимыми интерфейсами работать вместе.

from abc import ABC, abstractmethod

class IScale(ABC):
    @abstractmethod
    def get_weight(self) -> float:
        ...
        
class RussianScale(IScale):
    def __init__(self, cw: float):
        self.__cur_weight=cw
        
    def get_weight(self) -> float:
        return self.__cur_weight
    
class BritishScale(IScale):
    def __init__(self, cw: float):
        self.__cur_weight=cw
        
    def get_weight(self) -> float:
        return self.__cur_weight
    
class AdapterBritishScale(IScale):
    def __init__(self, british_scale: BritishScale):
        self.__british_scale=british_scale
    
    def get_weight(self) -> float:
        return self.__british_scale.get_weight()*0.453

def main() -> None:
    
    kg: float=55.6
    lb: float=55.6
    
    rScale=RussianScale(cw=kg)
    bScale=AdapterBritishScale(british_scale=BritishScale(cw=lb))
    
    print(rScale.get_weight(), 'kg')
    print(bScale.get_weight(), 'lb -> kg')
    

if __name__ == '__main__':
    main()