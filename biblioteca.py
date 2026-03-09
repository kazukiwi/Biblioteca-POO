class Biblioteca():
    def __init__(self):
        self.__lista = []

    def adicionar_item(self, item):
        self.__lista.append(item)
        print(f"Item '{item.get_titulo()}' adicionado com sucesso.")

    def listar_itens(self):
        if not self.__lista:
            print("Nenhum item cadastrado.")
        for item in self.__lista:
            item.exibir_detalhes()

    def buscar_por_codigo(self, codigo):
        for item in self.__lista:
            if item.get_codigo() == codigo:
                return item
        return None
    
    def emprestar_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.emprestar()
        else:
            print("Item não encontrado")

    def devolver_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.devolver()
        else:
            print(f"Item com código {codigo} não encontrado.")