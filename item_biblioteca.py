from abc import ABC, abstractmethod

class Item_biblioteca(ABC):
    def __init__(self, codigo: str, titulo: str, ano: int):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = True
    
    @abstractmethod
    def exibir_detalhes(self):
        print(f"Código: {self.__codigo}\n"
              f"Titulo: {self.__titulo}\n"
              f"Ano: {self.__ano}\n"
              f"Disponibilidade: {self.__disponivel}")

    def emprestar(self, disponivel = True):
        if disponivel == True:
            print(f"O livro foi emprestado com sucesso")
            self.__disponivel = False
        else:
            print(f"O livro já está sendo emprestando 😢")

    def devolver(self, disponivel = False):
        if disponivel == False:
            self.__disponivel = True
            print(f"O livro foi devolvido com sucesso!")
        else:
            print(f"O livro já foi devolvido!")

    def set_codigo(self, codigo: int):
        if codigo > 0:
            self.__codigo = codigo
        print(f"Código invalido! {codigo} deve ser maior que 0")

    def set_titulo(self, titulo: str):
        if not titulo.strip():
            print(f"O título está vazio ou contém apenas espaços")
        self.__titulo = titulo
        print(f"Titulo {titulo} cadastrado!")
    
    def set_ano(self, ano: int):
        if ano > 0:
            self.__ano = ano
            print(f"Ano cadastrado!")
        print(f"Ano invalido!")

    def get_codigo(self):
        return self.__codigo
    
    def get_titulo(self):
        return self.__titulo
    
    def get_ano(self):
        return self.__ano
    
    def get_disponivel(self):
        return self.__disponivel