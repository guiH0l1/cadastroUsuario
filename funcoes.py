def perguntar():
    return input("o que deseja realizar?\n" +
          "<I> - Para Inserir um usuário\n" +
          "<P> - Para Pesquisar um usuário\n" +
          "<E> - Para Excluir um usuário\n" +
          "<L> - Para Listar um usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a ultima data de acesso: "),
                                                     input("Qual a area do funcionário: ").upper()]
    salvar(dicionario)

def salvar (dicionario):
    with open("../meus projetos python/dicionario/bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

def pesquisar(dicionario):
        pesquisar = input("Digite o login do usuário: ").upper()
        if pesquisar in dicionario:
            print("\tLogin: ", pesquisar)
            print("\tNome: ", dicionario[pesquisar][0])
            print("\tUltima data de acesso: ", dicionario[pesquisar][1])
            print("\tArea do funcionário: ", dicionario[pesquisar][2])
        else:
            print("Usuário não encontrado!")

def excluir(dicionario):
    pesquisar = input("Digite o usuário a ser excluido: ").upper()
    if pesquisar in dicionario:
         del dicionario[pesquisar]
         print("Excluído")
    else:
         print("Usuário não encontrado!")

def listar(dicionario):
    print("Listagem de usuários:")
    for login, info in dicionario.items():
        print("\tLogin:", login)
        print("\tNome", info[0])
        print("\tUltima data de acesso:", info[1])
        print("\tArea do funcionário:", info[2])
        print("------------------------")
