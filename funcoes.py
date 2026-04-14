import json

ARQUIVO = "chamados.json"

def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def abrir_chamado():
    dados = carregar()

    titulo = input("Título do problema: ")
    descricao = input("Descrição: ")

    chamado = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Aberto"
    }

    dados.append(chamado)
    salvar(dados)

    print("✅ Chamado aberto!")

def listar_chamados():
    dados = carregar()

    if not dados:
        print("Nenhum chamado.")
        return

    for i, c in enumerate(dados):
        print(f"\nID: {i}")
        print(f"Título: {c['titulo']}")
        print(f"Descrição: {c['descricao']}")
        print(f"Status: {c['status']}")

def atualizar_status():
    dados = carregar()
    listar_chamados()

    try:
        i = int(input("\nID do chamado: "))
        print("1 - Aberto")
        print("2 - Em andamento")
        print("3 - Resolvido")

        op = input("Novo status: ")

        if op == "1":
            dados[i]["status"] = "Aberto"
        elif op == "2":
            dados[i]["status"] = "Em andamento"
        elif op == "3":
            dados[i]["status"] = "Resolvido"

        salvar(dados)
        print("🔄 Status atualizado!")
    except:
        print("Erro.")

def excluir_chamado():
    dados = carregar()
    listar_chamados()

    try:
        i = int(input("\nID para excluir: "))
        dados.pop(i)

        salvar(dados)
        print("❌ Chamado excluído!")
    except:
        print("Erro.")