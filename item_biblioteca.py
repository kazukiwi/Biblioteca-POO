from abc import ABC, abstractmethod

class Item_biblioteca(ABC):
    def __init__(self, codigo: str, titulo: str, ano: int, disponivel: bool):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel
    
    @abstractmethod
    def exibir_detalhes(self):
        pass

