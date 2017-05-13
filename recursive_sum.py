

def Suma(num1, num2):
    if num2 == 1:
        return num1 + 1
    else:
        return num1 + Suma(1, num2 - 1)


if __name__ == '__main__':
    numero1 = int(raw_input('Enter a number: '))
    numero2 = int(raw_input('Enter a number: '))

    print('{} + {} = {}'.format(numero1, numero2, Suma(numero1, numero2)))
