from item_biblioteca import Item_biblioteca

class Livro(Item_biblioteca):
    def __init__(self, codigo, titulo, ano, disponivel, autor: str, num_paginas: int):
        super().__init__(codigo, titulo, ano, disponivel)
        self.item = "Livro"
        self.__autor = autor
        self.__num_paginas = num_paginas

    def exibir_detalhes(self):
        print(f"Item Biblioteca: {self.item}")
        super().exibir_detalhes()
        print(f"Autor: {self.__autor}\n"
              f"Numero de Páginas: {self.__num_paginas}")
        