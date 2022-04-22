
""" Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para 
esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e 
pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram 
ignorados. Faça um programa que leia uma sequência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""

terminal = input()

if str(terminal) != "" :
        if str(terminal) == str(terminal)[::-1] :
            print("Palindrome")
        else:
            print("Não e Palindromo")