#que leia um ano qualquer e mostre se ele é bissexto ano
import calendar
from datetime import date
ano = int(input('Diga o ano, ou coloque 0 para analisar o ano atual:'))
if ano==0:
    ano= date.today().year
if calendar.isleap(ano):
    print(f'o ano de: {ano} é bissexto')
else :
    print(f'o ano de: {ano} não é bissexto')
