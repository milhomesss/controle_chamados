from funcoes import *

while True:
    print("\n=== SISTEMA DE CHAMADOS ===")
    print("1 - Abrir chamado")
    print("2 - Listar chamados")
    print("3 - Atualizar status")
    print("4 - Excluir chamado")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        abrir_chamado()
    elif op == "2":
        listar_chamados()
    elif op == "3":
        atualizar_status()
    elif op == "4":
        excluir_chamado()
    elif op == "0":
        break
    else:
        print("Opção inválida")