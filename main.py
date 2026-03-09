from biblioteca import Biblioteca
from livro import Livro
from revista import Revista

biblioteca = Biblioteca()

while True:
    print("\nMenu Biblioteca 📚")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Revista")
    print("3. Listar Itens")
    print("4. Emprestar Item")
    print("5. Devolver Item")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = int(input("Código: "))
        titulo = input("Título: ")
        ano = int(input("Ano: "))
        autor = input("Autor: ")
        num_paginas = int(input("Número de páginas: "))

        livro = Livro(codigo, titulo, ano, autor, num_paginas)
        biblioteca.adicionar_item(livro)

    elif opcao == "2":
        codigo = int(input("Código: "))
        titulo = input("Título: ")
        ano = int(input("Ano: "))
        edicao = input("Edição: ")
        mes = input("Mês: ")

        revista = Revista(codigo, titulo, ano, edicao, mes)
        biblioteca.adicionar_item(revista)

    elif opcao == "3":
        biblioteca.listar_itens()

    elif opcao == "4":
        codigo = int(input("Código do item: "))
        biblioteca.emprestar_item(codigo)

    elif opcao == "5":
        codigo = int(input("Código do item: "))
        biblioteca.devolver_item(codigo)

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")