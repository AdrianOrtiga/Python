# -*- coding: utf-8 -*-
"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):

    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
            print("No esta entre las repetidas, {}".format(seen_letters[letter]))
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)
            print("¡Repetida!, cuento {}".format(seen_letters[letter]))

    final_letters = []

    for key, value in seen_letters.iteritems():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )
            print("Añadimos: {}".format(final_letters))

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])
    print("ordenamos el diccionario: {}".format(not_repeated_letters))

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
