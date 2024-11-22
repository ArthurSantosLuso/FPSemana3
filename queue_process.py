from collections import deque

frases = input("")

# inicializar a stack
stack = deque()

for palavra in frases.split()[::-1]:
    stack.append(palavra)

print(stack)

# imprimir cada elemento da stack multiplicado por 2
while stack:
    palavra = stack.pop()
    if 'a' in palavra:
        print(palavra)