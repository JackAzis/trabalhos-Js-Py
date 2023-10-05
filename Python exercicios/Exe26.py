#um programa que leia uma frase pelo teclado e mostre
#quantas vezes aparece a letra 'a' em que posição ela aparece a primeira vez e em que vez aparece a ultima
f = str(input('Digite uma frase: ')).lower().strip()
print(f"sua frase tem {f.count('a')} vogais a\nela aparece primeiro na casa:{f.find('a')+1}\n"
      f"e aparece por ultimo na casa: {f.rfind('a')+1}")
