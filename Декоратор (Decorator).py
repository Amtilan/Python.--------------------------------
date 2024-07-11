# Тут рассмотрен пример структурного шаблона проектирования программ «Декоратор», 
# предназначенный для динамического подключения объекту дополнительного поведения. 
# Шаблон «Декоратор» предоставляет гибкую альтернативу практике создания подклассов с целью расширения функциональности.

from abc import ABC, abstractmethod
from dataclasses import dataclass


class IProcessor(ABC):
    @abstractmethod
    def process(self) -> None:
        ...
        
@dataclass
class Transmitter(IProcessor):
    data: str
    def process(self) -> None:
        print(f'Данные {self.data=} переданы по каналу связи')

@dataclass    
class Shell(IProcessor):
    processor: IProcessor
    
    @abstractmethod
    def process(self) -> None:
        self.processor.process()

@dataclass
class HammingCoder(Shell):
    def process(self) -> None:
        print('Наложен помехоустойчивый код Хэмминга->', end='')
        self.processor.process()
       
@dataclass 
class Encryptor(Shell):
    def process(self) -> None:
        print('Шифрование данных->', end='')
        self.processor.process()

def main() -> None: 
    transmitter: IProcessor=Transmitter(data='Какие-то данные')
    transmitter.process()
    print()
    
    hamming_coder: Shell=HammingCoder(processor=transmitter)
    hamming_coder.process()
    print()
    
    encryptor: Shell=Encryptor(processor=hamming_coder)
    encryptor.process()
    
if __name__ == "__main__":
    main()
