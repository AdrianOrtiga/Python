# -*- coding: utf-8 -*-

valor_bits = {0: 1, 1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7:128}

def cypher(message):
    cypher_message = []

    for letter in message:
        cypher_message.append(bin(ord(letter)))
        cypher_message.append(' ')

    return ' '.join(cypher_message)


def decipher(message):
    code = message.split(' ')
    decipher_message = []
    cadena = ""

    for digits in code:
      binario = digits[::-1]
      suma = 0;

      for posicion in range(len(binario)):
          if binario[posicion] == '1':
             suma += valor_bits[posicion]

      if suma>0:
         cadena += chr(suma)

    return cadena


def run():

    while True:

        command = str(raw_input('''--- * --- * --- * --- * --- * --- * --- * ---

            Welcome to binary cypher. Wish do you do?

            [c]ypher message
            [d]ecypher message
            [e]xit
        '''))

        if command == 'c':
            message = str(raw_input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(raw_input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 'e':
            print('exit')
        else:
            print('Up! Wrong comand... ')


if __name__ == '__main__':
    print('B I N E I T O R')
    run()
