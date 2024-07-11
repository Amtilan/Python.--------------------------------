# Тут рассмотрен пример структурного шаблона проектирования программ «Адаптер», 
# предназначенный для организации использования функций объекта, недоступного для модификации, 
# через специально созданный интерфейс. Другими словами, он позволяет объектам с несовместимыми интерфейсами работать вместе.

from abc import ABC, abstractmethod
from dataclasses import dataclass

class IScales(ABC):
    @abstractmethod
    def get_weight(self) -> float:
        ...
    
    @abstractmethod
    def adjust(self) -> None:
        ...

@dataclass
class RussianScales(IScales):
    current_weight: float
    
    def get_weight(self) -> float:
        return self.current_weight
    
    def adjust(self) -> None:
        print('Регулирование Российских весов')
        
@dataclass
class BritishScales(IScales):
    current_weight: float
    
    def get_weight(self) -> float:
        return self.current_weight
    
    def adjust(self) -> None:
        print('Регулирование British весов', end=' ')

class AdapterForBritishScales(BritishScales, IScales):
    def __init__(self, cw: float):
        super().__init__(cw)
        
    def get_weight(self) -> float:
        return super().get_weight() * 0.453

    def adjust(self) -> None:
        super().adjust()
        print('в методе регулировки adjust() адаптера')

def main() -> None:
    rScales: IScales=RussianScales(current_weight=55.)
    bScales: IScales=AdapterForBritishScales(cw=55.)
    print(rScales.get_weight())
    print(bScales.get_weight())
    
    rScales.adjust()
    bScales.adjust()
    
    
if __name__ == "__main__":
    main()