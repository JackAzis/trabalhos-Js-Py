import requests
import os

def limpar_tela():
    '''limpa a tela, para mostrar a função seguinte'''
    os.system('cls')

def voltar_ao_menu_principal():
    '''Voltar ao menu principal'''
    input('\nDigite uma tecla para retornar ao menu: ')
    main()

def exibir_opcoes():
    '''mostra opções do menu inicial'''
    print('1. Cotação do Dolar', '2. Cotação do Euro', 
          '3. Cotação do Bitcoin', '4. Cotação de periodo especifico\n', sep='\n')

def opcoes_iniciais():
    '''area de seleção das opções de moeda e cotação em uma data especifica'''
    try:
        selecao = int(input(f'Digite uma opção: '))
        print(f'Você escolheu a opção {selecao}')
        match selecao:
            case 1:
                cotacoes('USDBRL')
            case 2:
                cotacoes('EURBRL')
            case 3:
                cotacoes('BTCBRL')
            case 4:
                limpar_tela()
                moeda_no_tempo = int(input(f'Selecione a moeda que deseja ver em um período específico\n1. Dolar\n2. Euro\n3. Bitcoin\n'))
            
                if moeda_no_tempo in [1, 2, 3]:
                    cotacao_especifica(['USD-BRL', 'EUR-BRL', 'BTC-BRL'][moeda_no_tempo - 1])
                else:
                    opcao_invalida()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def cotacao_especifica(moeda):
    '''colhe data especifica para de moeda já selecionada anteriormente, para cotação de dia especifico '''
    dia = input('Digite o dia: ')
    mes = input('Digite o mês: ')
    ano = input('Digite o ano: ')
    
    end_date = ano+mes+dia
    '''solicitação na api e seleção da lista e dicionario'''
    cotacoes_especificas = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{moeda}/?start_date=10000101&end_date={end_date}')
    dia_especifico = cotacoes_especificas.json()
    dia_especifico = dia_especifico[0]['bid']
    
    '''resposta para cada moeda especifica'''
    if moeda == 'USD-BRL':
        limpar_tela()
        print(f'A cotação do Dolar neste período foi de: \n{dia_especifico}')
    elif moeda == 'EUR-BRL':
        limpar_tela()
        print(f'A cotação do Euro neste período foi de: \n{dia_especifico}')
    elif moeda == 'BTC-BRL':
        limpar_tela()
        print(f'A cotação do bitcoin neste período foi de: \n{dia_especifico}')

    print(f'Carregando cotação de {dia}/{mes}/{ano}')

def opcao_invalida():
    '''caso informada entrada errada limpa a tela e solicita nova entrada'''
    limpar_tela()
    print(f'Entrada errada, por favor selecione uma das opções válidas\n')

def cotacoes(moeda, tipo='bid'):
    '''solicitação a api da cotação mais recente de compra e venda para moeda especifica'''
    cotacoes_agora = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao_agora = cotacoes_agora.json()
    
    moeda_agora_compra = cotacao_agora[moeda] [tipo]
    moeda_agora_venda = cotacao_agora[moeda] ['ask']
    if moeda == 'USDBRL':
        limpar_tela()
        print(f'A cotação do Dolar neste momento é de: \n{moeda_agora_compra} para compra \n{moeda_agora_venda} para venda')
        

    elif moeda == 'EURBRL':
        limpar_tela()
        print(f'A cotação do Euro neste momento é de: \n{moeda_agora_compra} para compra \n{moeda_agora_venda} para venda')

    elif moeda == 'BTCBRL':
        limpar_tela()
        print(f'A cotação do bitcoin neste momento é de: \n{moeda_agora_compra} para compra \n{moeda_agora_venda} para venda') 

def main():
    limpar_tela()
    exibir_opcoes()
    opcoes_iniciais()
    voltar_ao_menu_principal()

if __name__ == '__main__':
    main()
