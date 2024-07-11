# Тут рассмотрен пример структурного шаблона проектирования программ «Компоновщик», 
# объединяющий объекты в древовидную структуру для представления иерархии. 
# «Компоновщик» позволяет клиентам обращаться к отдельным объектам и к группам объектов одинаково.

from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Item(ABC):
    item_name: str
    owner_name: Optional[str] = None
    def set_owner(self, owner: str) -> None:
        self.owner_name=owner
    @abstractmethod
    def add(self, sub_item: 'Item') -> None:
        ...
    @abstractmethod
    def remove(self, sub_item: 'Item') -> None:
        ...
    @abstractmethod
    def display(self) -> None:
        ...

@dataclass
class ClickableItem(Item):
    def add(self, sub_item: Item) -> None:
        raise Exception('Кликабельному элементу нельзя добавить подэлемент')
    def remove(self, sub_item: Item) -> None:
        raise Exception('У Кликабельного элемента не могут быть подэлементы')
    def display(self) -> None:
        print(f"{self.owner_name} {self.item_name}" if self.owner_name else self.item_name)
        
@dataclass
class DropDownItem(Item):
    children: List[Item] = field(default_factory=list)
    def add(self, sub_item: Item) -> None:
        sub_item.set_owner(self.item_name)
        self.children.append(sub_item)
    
    def remove(self, sub_item: Item) -> None:
        self.children.remove(sub_item)
    
    def display(self) -> None:
        for item in self.children:
            if self.owner_name is not None:
                print(self.owner_name, end=' ')
            item.display()

def main() -> None:
    file: Item=DropDownItem(item_name='Файл->')
    create: Item=DropDownItem(item_name='Создать->')
    open_: Item=DropDownItem(item_name='Открыть->')
    exit_: Item=ClickableItem(item_name='Выход')
    
    file.add(sub_item=create)
    file.add(sub_item=open_)
    file.add(sub_item=exit_)
    
    project: Item=ClickableItem(item_name='Проект...')
    repisitory: Item=ClickableItem(item_name='Репизиторий...')
    
    create.add(project)
    create.add(repisitory)
    
    solution: Item=ClickableItem(item_name='Решение...')
    folder: Item=ClickableItem(item_name='Папка...')
    
    open_.add(solution)
    open_.add(folder)
    
    file.display()
    print('\nУдаление клибельного элемента create')
    
    file.remove(create)
    file.display()
    
if __name__ == "__main__":
    main()