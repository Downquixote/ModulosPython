# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
cco = float(input('Digite o Comprimento do Cateto Oposto: '))
cca = float(input('Digite o Comprimento do Cateto Adjacente: '))
hi = hypot(cco, cca)

print('O comprimento da Hipotenusa irá medir {:.2f}'.format(hi))