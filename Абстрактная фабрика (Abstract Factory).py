# Тут рассмотрен пример порождающего шаблона проектирования программ «Абстрактная фабрика», 
# который предоставляет интерфейс взаимосвязанных или взаимозависимых объектов, не специфицируя их конкретных классов. 
# Шаблон применяется в случаях, когда программа должна быть не зависимой от процессов и типов создаваемых новых объектов, 
# а также, когда необходимо создавать группы взаимосвязанных объектов.

from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self) -> None:
        pass
    
class KazakhEngine(IEngine):
    def release_engine(self) -> None:
        print('Camry 70 посчитаем что казахский двигатель')
        
class ChineseEngine(IEngine):
    def release_engine(self) -> None:
        print('Chinese engine')
        
        
        
class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, engine: IEngine) -> None:
        pass
    
class KazakhCar(ICar):
    def release_car(self, engine: IEngine) -> None:
        print('Kazakh car', end=' ')
        engine.release_engine()

class ChineseCar(ICar):
    def release_car(self, engine: IEngine) -> None:
        print('Chinese Car', end=' ')
        engine.release_engine()
       
       
       
class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass
    @abstractmethod
    def create_car(self) -> ICar:
        pass
    
class KazakhFactory(IFactory):
    def create_engine(self) -> IEngine:
        return KazakhEngine()
    def create_car(self) -> ICar:
        return KazakhCar()
    
class ChineseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return ChineseEngine()
    def create_car(self) -> ICar:
        return ChineseCar()
 
 
 
def main() -> None:
    Kazakh_Factory=KazakhFactory()
    Kazakh_Engine=Kazakh_Factory.create_engine()
    Kazakh_Car=Kazakh_Factory.create_car()
    Kazakh_Car.release_car(engine=Kazakh_Engine)
    
    Chinese_factory=ChineseFactory()
    Chinese_Engine=Chinese_factory.create_engine()
    Chinese_Car=Chinese_factory.create_car()
    Chinese_Car.release_car(engine=Chinese_Engine)
    
if __name__ == "__main__":
    main()