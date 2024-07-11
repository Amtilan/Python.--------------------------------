# Тут рассмотрен пример порождающего шаблона проектирования программ «Одиночка», 
# который гарантирует, что в приложении будет создан единственный экземпляр некоторого класса 
# и предоставляет глобальную точку доступа к этому экземпляру.

class DataBaseHepler:
    __database_connection = None
    __data: str=''
    def __new__(cls) -> 'DataBaseHepler':
        if cls.__database_connection is None:
            cls.__database_connection: DataBaseHepler=object.__new__(cls)
            print('Database connection')
        return cls.__database_connection
    
    def select_data(self) -> str:
        return self.__data
    
    def insert_data(self, new_data: str) -> None:
        self.__data=new_data
        
def main() -> None:
    first_con=DataBaseHepler()
    first_con.insert_data('Hello World!')
    
    second_con=DataBaseHepler()
    print(second_con.select_data())
    
if __name__ == '__main__':
    main()