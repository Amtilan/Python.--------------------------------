# Тут рассмотрен пример порождающего шаблона проектирования программ «Строитель», 
# который предоставляет способ создания составного объекта. 
# Он отделяет конструирование сложного объекта от его представления так, 
# что в результате одного и того же процесса конструирования могут получаться разные представления.

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Phone:
    data: str=''
    def about_phone(self) -> str:
        return self.data
    def append_data(self, data: str) -> None:
        self.data += data
        
class IDeveloper(ABC):
    @abstractmethod
    def create_display(self) -> None:
        ...
    @abstractmethod
    def create_box(self) -> None:
        ...
    @abstractmethod
    def system_install(self) -> None:
        ...
    @abstractmethod
    def get_phone(self) -> Phone:
        ...
    
    
class AndroidDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()
    def create_display(self) -> None:
        self.__phone.append_data('Samsung Phone Display created successfully; ')
    def create_box(self) -> None:
        self.__phone.append_data('Samsung Phone Frame created successfully; ')
    def system_install(self) -> None:
        self.__phone.append_data('Samsung Phone System installed successfully; ')
    def get_phone(self) -> Phone:
        return self.__phone

class IphoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()
    def create_display(self) -> None:
        self.__phone.append_data('iPhone Phone Display created successfully; ')
    def create_box(self) -> None:
        self.__phone.append_data('iPhone Phone Frame created successfully; ')
    def system_install(self) -> None:
        self.__phone.append_data('iPhone System Installed successfully; ')
    def get_phone(self) -> Phone:
        return self.__phone
    
@dataclass
class Director:
    developer: IDeveloper = field(default=None)
    
    def set_developer(self, developer: IDeveloper) -> None:
        self.developer=developer
    def mount_only_phone(self) -> Phone:
        self.developer.create_box()
        self.developer.create_display()
        return self.developer.get_phone()
    def mount_full_phone(self) -> Phone:
        self.developer.create_box()
        self.developer.create_display()
        self.developer.system_install()
        return self.developer.get_phone()


def main() -> None:
    Android_Developer: IDeveloper=AndroidDeveloper()
    director = Director(developer=Android_Developer)
    samsung: Phone=director.mount_full_phone()
    print(samsung.about_phone())
    
    Iphone_Developer: IDeveloper=IphoneDeveloper()
    director.set_developer(developer=Iphone_Developer)    
    iphone: Phone=director.mount_only_phone()
    print(iphone.about_phone())


if __name__ == '__main__':
    main()