# Тут рассмотрен пример структурного шаблона проектирования программ «Мост». 
# Он используется в проектировании программного обеспечения, разделяя абстракцию и реализацию так,
# чтобы они могли изменяться независимо. Шаблон «Мост» использует инкапсуляцию, 
# агрегирование и может использовать наследование для того, чтобы разделить ответственность между классами.

import abc
from dataclasses import dataclass

class IDataReader(abc.ABC):
    @abc.abstractmethod
    def read(self) -> None:
        ...

class DataBaseReader(IDataReader):
    def read(self) -> None:
        print('Данные из базы данных(бд) ', end='')
        
class FileReader(IDataReader):
    def read(self) -> None:
        print('Данные из файла ', end='')
    
@dataclass
class Sender(abc.ABC):
    reader: IDataReader
    def set_data_reader(self, data_reader: IDataReader) -> None:
        self.reader: IDataReader=data_reader
    
    @abc.abstractmethod
    def send(self) -> None:
        ...

@dataclass  
class EmailSender(Sender):
    def send(self) -> None:
        self.reader.read()
        print('отправлен по электронной почте ')

@dataclass  
class TGbotSender(Sender):
    def send(self) -> None:
        self.reader.read()
        print('отправлен при помощи телеграмм бота ')
        
def main() -> None:
    sender: Sender=EmailSender(reader=DataBaseReader())
    sender.send()
    
    sender.set_data_reader(data_reader=FileReader())
    sender.send()
    
    sender: Sender=TGbotSender(reader=DataBaseReader())
    sender.send()

if __name__ == '__main__':
    main()