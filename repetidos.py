"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):

    for idx, char in enumerate(char_sequence):
        duplicate = False

        for c in (char_sequence[idx + 1: len(char_sequence)]):
            if char == c:
                duplicate = True
                break

        for c in (char_sequence[0: idx - 1]):
            if char == c:
                duplicate = True
                break

        if duplicate == False:
            return char

    return '_'


if __name__ == '__main__':
    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
