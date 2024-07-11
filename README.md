# Паттерны проектирования на Python

Этот проект демонстрирует использование различных паттернов проектирования на языке Python. Каждый паттерн представлен отдельным файлом и реализует определённую концепцию проектирования, чтобы сделать код более гибким и масштабируемым.

## Содержание

1. [Абстрактная фабрика (Abstract Factory)](#абстрактная-фабрика-abstract-factory)
2. [Одиночка (Singleton)](#одиночка-singleton)
3. [Прототип (Prototype)](#прототип-prototype)
4. [Строитель (Builder)](#строитель-builder)
5. [Фабричный метод (Factory Method)](#фабричный-метод-factory-method)

## Абстрактная фабрика (Abstract Factory)

Паттерн "Абстрактная фабрика" предоставляет интерфейс для создания семейств связанных или зависимых объектов без указания их конкретных классов. Этот паттерн позволяет создавать различные конфигурации объектов, которые могут взаимодействовать друг с другом.

Пример использования:
```python
# Абстрактная фабрика
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
