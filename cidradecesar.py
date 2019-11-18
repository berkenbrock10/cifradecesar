# -*- coding: utf-8 -*-
import sys
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
rotacao = 5

#Essa função serve tanto para encriptar, quanto pra decriptar.
#(msg) = mensagem e (dir) = direção.
def cifra(msg, dir):
    #Variavel para retornar a string.
    v = ''
    #Para cada letra ("c" = caracter) da msg, "pegamos" o indice do alfabeto (c_index).
    for c in msg:
        #Verificação para espaço " ", o espaço não pertence ao alfabeto então ele verifica aqui.
        # Se não pertence ao alfabeto ele não entra no if, ele vai entrar no else.
        if c in alfabeto:
            c_index = alfabeto.index(c)
            #Temos que usar o mod (%) dividindo pelo tamanho (len) do alfabeto. Por exemplo, quando chegar na 
            # letra y do alfabeto e for somar 5 pra "frente", não quebre a execução.
            v += alfabeto[(c_index + (dir * rotacao)) % len(alfabeto)]
        #Ele apenas adiciona o espaço entre as letras aqui. (Isso também funciona com , ou . usei o espaço apenas como exemplo).
        else:
            v += c
    return v

def encriptar(msg):
    #O (1) significa que é pra andar para direita, no caso, é positivo.
    return cifra(msg, 1)

def desencriptar(msg):
    #O (-1) significa que é pra andar para esquerda, no caso, é negativo.
    return cifra(msg, -1)

#As 3 linhas abaixo são esqueleto padrão do python.
def main():
    #sys.argv[1] é primeiro parâmetro
    comando = sys.argv[1].lower()
    #sys.argv[2] é segundo parâmetro
    msg = sys.argv[2].lower()

    #Aqui é apenas para exibir a mensagem no console.
    if comando == 'encriptar':
        print encriptar(msg)
    elif comando == 'desencriptar':
        print desencriptar(msg)
    else:
        print comando + ' ---> COMANDO NÃO ENCONTRADO!!!'

if __name__ == '__main__':
    main()