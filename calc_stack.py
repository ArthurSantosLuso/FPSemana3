from collections import deque


numeros = input("")

# inicializar a stack
stack = deque()

for valor in numeros.split():
    stack.append(int(valor))

print(stack)

# imprimir cada elemento da stack multiplicado por 2
while stack:
    numero = stack.pop()
    print(numero * 2)