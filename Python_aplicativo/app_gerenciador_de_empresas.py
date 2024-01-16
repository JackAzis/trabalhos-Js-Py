import os

empresas = [{'nome':'LogiTech', 'categoria':'periféricos', 'ativo':True},   
            {'nome':'Xpg', 'categoria':'memorias', 'ativo':False},
            {'nome':'corsair', 'categoria':'informatica', 'ativo':False}]

def nome_do_programa():
    print("""
        
██╗░░██╗██╗░░░██╗██████╗░░█████╗░███╗░░░███╗░█████╗░████████╗░██████╗██╗░░░██╗
██║░██╔╝██║░░░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██╔════╝██║░░░██║
█████═╝░██║░░░██║██████╔╝██║░░██║██╔████╔██║███████║░░░██║░░░╚█████╗░██║░░░██║
██╔═██╗░██║░░░██║██╔══██╗██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░░╚═══██╗██║░░░██║
██║░╚██╗╚██████╔╝██║░░██║╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░██████╔╝╚██████╔╝
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░╚═════╝░
            """)

def exibir_opcoes():
    '''mostra opções do menu inicial'''
    print('1. Cadastrar empresa', '2. Listar empresas', 
          '3. Status da empresa', '4. Sair\n', sep='\n' )


def cadastrar_nova_empresa():
    '''Cadastra novas empresas'''
    exibir_subtitulo('Cadastro de novas empresas')
    nome_da_empresa = input('Digite o nome da empresa que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria da empresa: {nome_da_empresa}: ')
    dados_da_empresa = {'nome':nome_da_empresa, 'categoria':categoria, 'situação':False}
    empresas.append(dados_da_empresa)
    print(f'A empresa {nome_da_empresa} foi adicionado com sucesso\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''Voltar ao menu principal'''
    input('\nDigite uma tecla para retornar ao menu: ')
    main()

def listar_empresas():
    '''Responsavel por mostrar restaurantes cadastrados'''
    exibir_subtitulo('Lista de Empresas')
    
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    for empresa in empresas:
        nome_empresa = empresa['nome']
        categoria = empresa['categoria']
        ativo = 'ativado' if empresa['ativo'] else 'desativado'
        print(f'{nome_empresa.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()
    
def alternar_estado_empresa():
    '''Altera estado das empresas cadastradas, de ativo para inativo'''
    exibir_subtitulo()
    nome_empresa = input('Digite o nome da empresa que deseja alterar o estado: ')
    empresa_encontrada = False

    for empresa in empresas:
        if nome_empresa == empresa['nome']:
            empresa_encontrada = True
            empresa['ativo'] = not empresa['ativo']
            mensagem = f'A empresa {nome_empresa} foi ativada com sucesso' if empresa['ativo'] else f'A empresa {nome_empresa} foi desativada com sucesso'
            print(mensagem)
    if not empresa_encontrada:
        print('Empresa não encontrada')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''seleciona opções do menu inicial'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}\n')

        match opcao_escolhida:
            case 1:
                cadastrar_nova_empresa()
            case 2:
                listar_empresas()
            case 3:
                alternar_estado_empresa()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def opcao_invalida():
    '''mostra erro ao selecionar opção inválida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def finalizar_app():
    '''Mensagem que informa finalização do aplicativo'''
    os.system('cls')
    print('Finalizando o aplicativo\n')
    
def exibir_subtitulo(texto):
    '''Função responsavel por mostrar cabeçalho das páginas'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def main():
    '''Função responsavel pelo programa'''
    os.system('cls')
    nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()



