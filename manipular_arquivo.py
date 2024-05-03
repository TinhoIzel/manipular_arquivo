# PROGRAMA PARA MEXER EM QUANTOS ARQUIVOS TXT VOCÊ QUISER

# E O PROGRAMA ITERE SOBRE CADA DADO NA LEITURA, ADIÇÃO E ALTERAÇÃO
# INDEPENDENTE DO ARQUIVO, QUANTIDADE DE DADOS, POSIÇÃO E TUDO MAIS...



# Não pode mudar, ou pelo menos não é indicado
LISTA_ARQUIVOS = 'lista_arquivos.txt'

class Arquivo:
# TRABALHANDO COM A LISTA DE ARQUIVOS!

# Mostrando lista de arquivos
    def ver_lista():
        with open(LISTA_ARQUIVOS,'r', encoding='utf-8') as lista:
            arquivos = lista.readlines()
        print("\nArquivos: ")
        for arquivo in arquivos:
            print(arquivo.replace('.txt\n',''))



# Criando arquivo na lista LISTA_ARQUIVOS
    def criar_lista():
        criar = False
        while(True):
            confirmacao = input("Deseja criar um arquivo? (S/N): ").capitalize()
            print()
            if (confirmacao == 'S'):
                criar = True
                break
            # Caso não, cancela
            elif (confirmacao == 'N'):
                break
            # Até responder s/n
            else:
                print("Entrada inválida!")
        
        # Caso sim
        if (criar):
            print("Criação de um arquivo")
            
            Arquivo.ver_lista()

            novo_arquivo = input("Digite o nome do arquivo: ")

            criar = True
            while (True):

                    # Checando se LISTA_ARQUIVOS já existe
                    try:
                        with open(LISTA_ARQUIVOS,'r', encoding='utf-8') as lista:
                            arquivos = lista.readlines()

                        # Checando se o arquivo já existe, se não, criar...
                        if (novo_arquivo + '.txt\n') in arquivos:
                            print("Arquivo já existe na lista!")
                            criar = False
                        break

                    # Caso a lista não exista, vai criar
                    except FileNotFoundError as e:
                        print("Lista não encontrada..")
                        with open(LISTA_ARQUIVOS, 'w', encoding='utf-8'):
                            print("CRIANDO LISTA...")
        
        # Preparando e formantando os dados
        if (criar):
            print("\nAgora digite os dados que o arquivo terá")
            print("Para parar, digite PARAR")
            print("Obs.: ID já está incluso...")
            
            q_dados = 0
            dados = 'Id'
            # Até parar
            while (True):
                q_dados += 1
                dado = input("Dado "+ str(q_dados) +": ")
                if (dado.upper() == 'PARAR'):
                    if (len(dados) != 2):
                        break
                    else:
                        print("Digite pelo menos um dado!!")
                else:
                    # Deixar bonitinho (espaço não importa, só o ;)
                    dado = ';'+ dado.capitalize()
                    dados = dados + dado
            
            # Criando e colocando os dados
            with open(LISTA_ARQUIVOS, 'a', encoding='utf-8') as lista:
                lista.write(novo_arquivo + '.txt\n')
            with open(novo_arquivo + '.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write(dados + '\n')
    


    def excluir_lista():
        print("\n\n\nEscolhendo arquivo para excluir")

        arquivos = []

        Arquivo.ver_lista()
        
        with open(LISTA_ARQUIVOS,'r', encoding='utf-8') as lista:
            arquivos = lista.readlines()

        arquivo_excluir = input("Digite o nome do arquivo a ser excluído (sem .txt): ")
        existe = False
        if (arquivo_excluir + '.txt\n') in arquivos:
            existe = True
            linha = 0
            for arquivo in arquivos:
                if (arquivo_excluir + '.txt\n') == arquivo:
                    break
                else:
                    linha += 1

        if (existe):
            # Confirmação da deleção kk
            while(True):
                confirmacao = input("Deseja realmente deletar? (S/N): ").capitalize()
                
                if (confirmacao == 'S'):

                    # Fazendo a cópia
                    with open(LISTA_ARQUIVOS, 'r', encoding='utf-8') as lista:
                        # puxando as linhas
                        linhas = lista.readlines()

                        # deletando a linha
                        del linhas[linha]

                    # Sobrepondo / deletando linha
                    with open(LISTA_ARQUIVOS, 'w', encoding='utf-8') as lista:
                        lista.writelines(linhas) # função pra sobrepor

                    print("Deletado com sucesso!")
                    break

                # Caso não, cancela
                elif (confirmacao == 'N'):
                    print("Não foi excluído!")
                    break
                # Até responder s/n
                else:
                    print("Entrada inválida!")
            
        else:
            print("Arquivo não existe!")
        


    # ESCOLHENDO O ARQUIVO A TRABALHAR
    # Criando o objeto arquivo...
    def __init__(self):
        print("\n\n\nEscolhendo arquivo para manipular")

        arquivos = []

        Arquivo.ver_lista()
        
        with open(LISTA_ARQUIVOS,'r', encoding='utf-8') as lista:
            arquivos = lista.readlines()

        while (True):
            existe = False
            arquivo_escolhido = input("Digite o nome do arquivo (sem o .txt): ")
            for arquivo_existente in arquivos:
                if (arquivo_escolhido == arquivo_existente.replace('.txt\n','')):
                    existe = True
                    break
                else:
                    pass
            if(existe):
                print("\n\nAbrindo arquivo...")
                break
            else:
                print("Arquivo não existe!! Tente de novo.\n")

        # Criando o objeto Arquivo
        lista_dados = []
        with open(arquivo_escolhido +'.txt', 'r', encoding='utf-8') as arquivo:
            dados_texto = arquivo.readline()
            lista_dados = [dado for dado in dados_texto.replace('\n','').split(';')]
        
        self.arquivo = arquivo_escolhido +'.txt'
        self.dados = lista_dados
        self.informacoes = {}
 


    # MANIPULANDO NO ARQUIVO!

    def ler_arquivo(self):

        # Pegar os dados do txt
        with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        # Tirar a primeira linha (dados)
        del linhas[0]

        # Iterar em cada linha (informacao)
        for linha in linhas:

            # lista com dados da linha
            dados_linha = [dado for dado in linha.replace('\n','').split(';')]

            # criando o dict (info) base (sem id)
            info = {}
            info.clear
            for index in range(1, len(dados_linha)):
                info[self.dados[index]] = dados_linha[index]

            # adicionando a info a self.informacoes[id]
            self.informacoes[dados_linha[0]] = info



    def mostrar_arquivo(self):
        # Mostrar de forma organizada
        self.ler_arquivo()
        
        # Tá vazio?
        if (not self.informacoes):
            print()
            print("Não há informações.")
            print()
            return 0
        
        for id in self.informacoes:
            print()
            print("Id: "+ id)

            for info in self.informacoes[id]:
                print(info +": "+ self.informacoes[id][info])
        print()
    


    def adicionar_arquivo(self):
        # Pedindo entrada do usuário
        print("Digite os dados da informação a adicionar")
        adicionar = []
        for index in range(1, len(self.dados)):
            dado = input(self.dados[index] +": ")
            adicionar.append(dado)

        # Confirmação da adição
        print("\nConfirmação da adição")
        for index in range(1, len(self.dados)):
            print(self.dados[index] +": "+ adicionar[index - 1])

        while(True):
            
            confirmacao = input("Deseja realmente adicionar? (S/N): ").capitalize()
            if (confirmacao == 'S'):

                # Obtendo o último id + 1
                self.ler_arquivo()
                id = str(int(list(self.informacoes)[-1]) + 1) if self.informacoes else '1001'

                # Formatando a linha
                nova_informacao = id + ';'
                nova_informacao += ';'.join(adicionar) +'\n'

                # Adicionando linha
                with open(self.arquivo, 'a', encoding='utf-8') as arquivo:        
                    arquivo.write(nova_informacao)
                print("Adicionado com sucesso!")
                self.mostrar_arquivo()
                break

            # Caso não, cancela
            elif (confirmacao == 'N'):
                print("Adição cancelada!")
                break
            # Até responder s/n
            else:
                print("Entrada inválida!")
                pass



    def alterar_arquivo(self):
        self.mostrar_arquivo()

        # Checando id se o Id existe e a linha do Id
        while(True):
            id_alterar = input("Digite o ID da informação a ser alterada: ")
            
            linha = 1   # index 1 da lista de readlines

            # Checando se o Id existe
            if id_alterar in self.informacoes:
                for id in list(self.informacoes):
                    if id == id_alterar: 
                        break 
                    else:
                        linha += 1
                break

            else:
                print("ID não encontrado!")
        
        # Guardando entradas do usuário
        print("\nDigite as informações a mudar (caso não queira alterar, passar em branco):")
        alterar = []
        for index in range(1, len(self.dados)):
            dado = input(self.dados[index] +": ")
            alterar.append(dado)

        # Montando a lista com dados não alterados para trabalhar
        dado_nao_alterado = []
        for dado in self.informacoes[id_alterar]:
            dado_nao_alterado.append(self.informacoes[id_alterar][dado])

        # Se passar vazio, recebe da lista
        for index in range(len(alterar)):
            alterar[index] = dado_nao_alterado[index] if alterar[index] == '' else alterar[index]

        # Mostrando pós alteração
        print("\nInformação pós alteração: ")
        for index in range(len(alterar)):
            print(self.dados[index + 1] +": "+ alterar[index])
        
        # Confirmação para alterar
        while(True):
            confirmacao = input("Deseja realmente alterar? (S/N): ").capitalize()

            if (confirmacao == 'S'):
                # Montando linha alterada
                alteracao = id_alterar + ';'
                alteracao += ';'.join(alterar) +'\n'
                print(alteracao)

                # Fazendo cópia do arquivo com alteracao
                with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
                    # puxando as linhas
                    linhas = arquivo.readlines()
                    # alterando a linha
                    linhas[linha] = alteracao
                # Salvando alteração
                with open(self.arquivo, 'w', encoding='utf-8') as arquivo:
                    # escrevendo de volta no arquivo, com a linha alterada
                    arquivo.writelines(linhas) # função pra sobrepor
                print("Alteração concluída!")
                self.mostrar_arquivo()
                break

            # Caso não, cancela
            elif (confirmacao == 'N'):
                print("Alteração não feita!")
                break

            # Até responder s/n
            else:
                print("Entrada inválida!")
       
    def deletar_arquivo(self):
        self.mostrar_arquivo()
        deletado = False

        # Checando id se o Id existe e a linha do Id
        while(True):
            id_deletar = input("Digite o ID da informação a ser deletada: ")
            
            linha = 1   # index 1 da lista de readlines

            # Checando se o Id existe
            if id_deletar in self.informacoes:
                for id in list(self.informacoes):
                    if id == id_deletar: 
                        break 
                    else:
                        linha += 1
                break

            else:
                print("ID não encontrado!")
            
        # Confirmação da deleção kk
        while(True):
            confirmacao = input("Deseja realmente deletar? (S/N): ").capitalize()
            if (confirmacao == 'S'):

                # Fazendo a cópia
                with open(self.arquivo, 'r', encoding='utf-8') as arquivo:
                    # puxando as linhas
                    linhas = arquivo.readlines()
                    
                    # deletando a linha
                    del linhas[linha]
                
                # Sobrepondo / deletando linha
                with open(self.arquivo, 'w', encoding='utf-8') as arquivo:
                    arquivo.writelines(linhas) # função pra sobrepor
                
                print("Deletado com sucesso!")

                # Alterando o objeto
                del self.informacoes[id_deletar]
                self.mostrar_arquivo()
                break

            # Caso não, cancela
            elif (confirmacao == 'N'):
                print("Não foi deletado!")
                break
            # Até responder s/n
            else:
                print("Entrada inválida!")


def lista(opcao):
    if(opcao == 'B'):
        Arquivo.criar_lista()
    if(opcao == 'C'):
        Arquivo.excluir_lista()



def manipular_arquivo(opcao):
    if(opcao == 'A'):
        ARQUIVO.mostrar_arquivo()
    if(opcao == 'B'):
        ARQUIVO.adicionar_arquivo()
    if(opcao == 'C'):
        ARQUIVO.alterar_arquivo()
    if(opcao == 'D'):
        ARQUIVO.deletar_arquivo()



if __name__ == "__main__":
    fechar_programa = False
    while(not fechar_programa):

        continuar = True
        while (continuar):
            Arquivo.ver_lista()
            print()
            print("Opções da lista:")
            print("A - Escolher arquivos")
            print("B - Criar arquivo")
            print("C - Excluir arquivo")
            print("D - Fechar programa")
            while (True):
                opcao = input("Opção escolhida: ").capitalize()

                opcoes = ['A','B','C']
                if (opcao == 'A'):
                    escolher = True
                    continuar = False

                if (opcao == 'D'):
                    print("Fechando programa")
                    continuar = False
                    fechar_programa = True
                    break

                if (opcao in opcoes):
                    lista(opcao)
                    break

                else:
                    print("Opção invalida")

        if fechar_programa:
            break
        
        if escolher:
            ARQUIVO = Arquivo()

        continuar = True
        while (continuar):
            print("\nOpções de manipulação do arquivo:")
            print("A - Mostrar informações")
            print("B - Adicionar informação")
            print("C - Alterar informação")
            print("D - Deletar informação")
            print("E - Voltar para as opções da lista")
            print("F - Fechar programa")
            while (True):
                opcao = input("Opção escolhida: ").capitalize()
                opcoes = ['A','B','C','D','E']
                if (opcao == 'F'):
                    print("Fechando programa")
                    continuar = False
                    fechar_programa = True
                    break

                # Voltando para opcoes da lista
                if (opcao == 'E'):
                    continuar = False
                    break

                if (opcao in opcoes):
                    manipular_arquivo(opcao)
                    break
                else:
                    print("Opção invalida")
