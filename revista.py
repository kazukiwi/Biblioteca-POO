from item_biblioteca import Item_biblioteca

class Revista(Item_biblioteca):
    def __init__(self, codigo, titulo, ano, edicao: int, mes: str):
        super().__init__(codigo, titulo, ano)
        self.item = "Revista"
        self.__edicao = edicao
        self.__mes = mes

    def exibir_detalhes(self):
        print(f"Item Biblioteca: {self.item}")
        super().exibir_detalhes()
        print(f"Autor: {self.__edicao}\n"
              f"Numero de Páginas: {self.__mes}")
        