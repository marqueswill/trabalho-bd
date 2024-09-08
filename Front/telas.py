from Front.helpers import *


def TelaInicial():
    limpar()

    linha()
    print("Tela Inicial")
    linha()
    opcoes = {
        0: "Sair",
        1: "CRUD",
    }
    for op in opcoes.items():
        print(f"{op[0]} - {op[1]}")
    try:
        escolha = int(input("Selecione uma opção: "))
    except ValueError:

        print("Entrada inválida, por favor, selecione uma opção válida.")
        return

    if escolha == 0:
        exit()
    elif escolha == 1:
        TelaEscolha()
    else:
        print("Opção inválida, tente novamente.")
        linha()


def TelaEscolha():
    limpar()
    linha()
    print("Escolha uma Entidade")
    linha()
    print(" 0 - Voltar\n")
    for number, e in entitites.items():

        print(f"{number:>2} - {e}")
    linha()
    try:
        escolha = int(input("Selecione uma entidade: "))
    except ValueError:

        print("Entrada inválida, por favor, selecione um número válido.")
        linha()
        return TelaEscolha()

    if escolha == 0:

        return TelaInicial()
    elif escolha not in entitites:

        print("Entidade inválida, tente novamente.")
        linha()
        return TelaEscolha()

    TelaCRUD(entitites[escolha])


def TelaCRUD(entidade):
    limpar()

    linha()
    print(f"CRUD de {entidade}")
    linha()

    opcoes = {
        0: "Voltar\n",
        1: "Criar",
        2: "Ler",
        3: "Atualizar",
        4: "Deletar",
    }
    for op in opcoes.items():
        print(f"{op[0]} - {op[1]}")
    try:
        escolha = int(input("Selecione uma operação: "))
    except ValueError:
        print("Entrada inválida, por favor, selecione uma opção válida.")
        linha()
        return

    if escolha == 0:
        return TelaEscolha()
    elif escolha == 1:
        TelaCreate(entidade)
    elif escolha == 2:
        TelaRead(entidade)
    elif escolha == 3:
        TelaUpdate(entidade)
    elif escolha == 4:
        TelaDelete(entidade)

    else:
        print("Opção inválida, tente novamente.")
        linha()


def TelaCreate(entidade):
    limpar()

    linha()
    print(f"Criando novo registro para {entidade}:")
    linha()

    value_obj = objetos[str(entidade)]
    valores = []
    for col in value_obj.columns():
        if col not in value_obj.auto_columns():
            if str(entidade) == "Compra" and col == '"notaFiscal"':
                print("notaFiscal: ")
                nome_arquivo = escolher_arquivo()
                entrada = entidade.get_as_bytea(nome_arquivo)
            else:
                entrada = input(col.replace('"', "") + ": ")

            if entrada == "":
                entrada = None
            valores.append(entrada)
        else:
            valores.append(None)
    linha()
    try:
        obj = generate_object(entidade, valores)
        entidade.insert(obj)

        input("Registro inserido com sucesso!")
        return TelaCRUD(entidade)
    except Exception as e:
        print(e)
        opcao = input("Não foi possível atualizar o registro! Deseja continuar? (S/N)")
        if opcao.lower() in ["s", "y"]:
            return TelaCreate(entidade)
        else:
            return TelaCRUD(entidade)


def TelaRead(entidade):
    limpar()

    linha()
    print(f"Lendo registros de {entidade}:")
    linha()
    registros = listar(entidade)
    # input("Aperte qualuqer tecla para voltar")
    linha()
    # return TelaCRUD(entidade)

    opcoes = {
        0: "Voltar",
        1: "Detalhar",
    }

    for op in opcoes.items():
        print(f"{op[0]} - {op[1]}")
    try:
        escolha = int(input("Selecione uma opção: "))
    except ValueError:
        return TelaRead(entidade)

    if escolha == 0:
        return TelaCRUD(entidade)
    elif escolha == 1:
        linha()
        index = input("Escolha o registro que deseja detalhar: ")
        registro = registros[int(index)]
        keys = [c.replace('"', "") for c in objetos[str(entidade)].columns()]
        values = registro.to_tuple()
        for k, v in zip(keys, values):
            print(f"{k} - {v}")

        if str(entidade) == "Compra":
            registro.export_pdf()

        input()
        return TelaRead(entidade)

    else:
        linha()
        print("Opção inválida, tente novamente.")
        input()
        return TelaRead(entidade)


def TelaUpdate(entidade):
    limpar()
    linha()
    listar(entidade)
    linha()
    escolha = input("Selecione o registro que deseja atualizar: ")
    print("Deixe em branco para manter o valor antigo")
    linha()
    try:
        selecionado = selecionar(entidade, escolha)

        valores = list(selecionado.to_tuple())

        for i, c in enumerate(selecionado.columns()):
            if c not in selecionado.keys():
                valor_input = input(c.replace('"', "") + ": ")
                if valor_input.strip() != "":
                    valores[i] = valor_input
        linha()

        print(f"Atualizando registro de {entidade}")
        atualizado = generate_object(entidade, valores)
        entidade.update(atualizado)

        input("Registro atualizado com sucesso!")
        return TelaCRUD(entidade)
    except Exception as e:
        print(e)
        opcao = input("Não foi possível atualizar o registro! Deseja continuar? (S/N)")
        if opcao.lower() in ["s", "y"]:
            return TelaUpdate(entidade)
        else:
            return TelaCRUD(entidade)


def TelaDelete(entidade):
    limpar()
    linha()
    listar(entidade)
    linha()
    escolha = input("Selecione o registro que deseja deletar: ")

    linha()

    try:
        selecionado = selecionar(entidade, escolha)
        print(f"Deletando registro de {entidade}")
        entidade.delete(selecionado)
        input("Registro deletado com sucesso!")
        return TelaCRUD(entidade)
    except:
        opcao = input("Não foi possível deletar o registro! Deseja continuar? (S/N)")
        if opcao.lower() in ["s", "y"]:
            return TelaDelete(entidade)
        else:
            return TelaCRUD(entidade)
