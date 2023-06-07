# Módulos são como bibliotecas.
# Temos duas maneiras pra carregar essas bibliotecas.
# Import math (carregará toda a biblioteca).
# from math import sqrt (carregará apenas o solicitado).
# para solicitar mais de dois módulos, basta pôr ','. Ex: from math import sqrt, ceil.

#import math

# Quando utilizar esse módulo, não é necessário escrever "math.sqrt". apenas "sqrt".
from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz quadradad de {} é {:.2f}'.format(num, raiz))

# math.ceil é utilizado para arredondar o número para cima.
#print('A raiz quadrada de {} é {}'.format(num, math.ceil(raiz)))

# math.floor é utilizado para arredondar o número para baixo
#print('A raiz quadrada de {} é {}'.format(num, math.floor(raiz)))

