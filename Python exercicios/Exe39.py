#leia o ano de nascimento de um jovem e informe, de acordo com a idade:
#e ele ainda vai se alistar ao serviço militar
#se é a hora de se alistar ou se já passou do tempo do alistamento
#dizendo o tempo que falta ou o que se passou
from datetime import date
nascimento = int(input('Em que ano você nasceu: '))
idade = date.today().year - nascimento
if idade == 18:
    print(f'Esta na hora de você se alistar')
elif idade < 18:
    print(f'Você vai precisar se alistar daqui a {18-idade} anos')
elif idade > 18:
    print(f'Você já deveria ter se alistado a {idade-18} anos')

