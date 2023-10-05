#um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo
import math
a = int(input('Qual é o angulo? '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print(f'o ângulo de {a}, tem:\n {seno:.2f} de seno\n {cos:.2f} de coseno e\n {tan:.2f} de tangente')