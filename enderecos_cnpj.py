import requests
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time

# esconde a janela do Tkinter
Tk().withdraw()

# abre menu de seleção de arquivo
caminho_arquivo = askopenfilename()

# confirma o arquivo e carrega o DataFrame
if caminho_arquivo:
    if caminho_arquivo.endswith('.csv'):
        df = pd.read_csv(caminho_arquivo)
    elif caminho_arquivo.endswith('.xlsx'):
        df = pd.read_excel(caminho_arquivo)
    elif caminho_arquivo.endswith('.json'):
        df = pd.read_json(caminho_arquivo)
    else:
        print('Arquivo em formato não suportado.')
        exit()

    # cabeçalho do DataFrame
    print('As colunas são:\n', df.columns.tolist())
else:
    print('Nenhum arquivo selecionado.')
    exit()

# consulta ao CNPJ na API da receita
def consultar_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    headers = {
        'Accept': 'application/json',
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'logradouro' in data:
                endereco = f"{data['logradouro']}, {data['numero']} - {data['bairro']}, {data['municipio']} - {data['uf']}, {data['cep']}"
                return endereco
            else:
                return "Endereço não encontrado."
        else:
            return "Erro ao consultar o CNPJ."
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"

# preenche os endereços no DataFrame
def preencher_enderecos(df, coluna_cnpj, coluna_endereco):
    # remove caracteres especiais do CNPJ
    df[coluna_cnpj] = df[coluna_cnpj].astype(str).str.replace(r'[./-]', '', regex=True)
    
    for index, row in df.iterrows():
        time.sleep(20) # a API só  permite 3 pesquisas por minuto
        cnpj = row[coluna_cnpj]
        # progressão
        print(f"Consultando CNPJ: {cnpj}")  
        endereco = consultar_cnpj(cnpj)
        df.at[index, coluna_endereco] = endereco
    return df

# input de CNPJ e endereço
coluna_cnpj = input('Digite o nome da coluna com os CNPJs: ')
coluna_endereco = input('Digite o nome da coluna de endereços para preenchimento: ')

# verifica se as colunas existem no DataFrame
if coluna_cnpj not in df.columns or coluna_endereco not in df.columns:
    print("Erro: Uma ou mais colunas informadas não existem no arquivo.")
    exit()

# preenche os endereços no DataFrame
df = preencher_enderecos(df, coluna_cnpj, coluna_endereco)

# salva o arquivo atualizado
if caminho_arquivo.endswith('.csv'):
    df.to_csv(caminho_arquivo, index=False)
elif caminho_arquivo.endswith('.xlsx'):
    df.to_excel(caminho_arquivo, index=False)
elif caminho_arquivo.endswith('.json'):
    df.to_json(caminho_arquivo, index=False)

print('Endereços preenchidos com sucesso!')
# exibe colunas CNPJ e endereço
print(df[[coluna_cnpj, coluna_endereco]])  
