n1 = float(input('Diga sua primeira nota: '))
n2 = float(input('Diga sua segunda nota: '))
m = (n1 +n2)/2
if m<=5:
    print('precisa melhorar')
else:
    print('parabens')
print(f'sua nota do teste foi {n1}\nde sua prova foi {n2}\nsua média é {m}')