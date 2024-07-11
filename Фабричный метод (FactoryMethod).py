# Тут расмотрен пример порождающего шаблона проектирования программ «Фабричный метод», 
# который предоставляет дочерним классам интерфейс для создания экземпляров некоторого класса. 
# В момент создания наследники могут определить какой класс создавать. 
# Это позволяет использовать в коде программы неспецифические классы, 
# а манипулировать абстрактными объектами на более высоком уровне.

class IProduct:
    def release(self):
        pass

class Car(IProduct):
    def release(self):
        print('Releasing car')
        
class Track(IProduct):
    def release(self):
        print('Releasing track')
        
        
class IWorkShop:
    def create(self) -> IProduct:
        pass
    
class CarWorkShop(IWorkShop):
    def create(self) -> IProduct:
        return Car()
    
class TrackWorkShop(IWorkShop):
    def create(self) -> IProduct:
        return Track()
    
    
def main() -> None:
    creator=CarWorkShop()
    car=creator.create()
    
    creator=TrackWorkShop()
    truck=creator.create()
    
    car.release()
    truck.release()
    
if __name__ == "__main__":
    main()