def calculaIMC(peso, numero):

    imc = float(peso) / float(numero) ** 2

    return imc

def verificaNivel(imc):

    if imc < 17:
        nivel = 'Muito abaixo do peso'
    elif 17 <= imc <= 18.49:
        nivel = 'Abaixo do peso'
    elif 18.5 <= imc <= 24.99:
        nivel = 'Peso normal'
    elif 25 <= imc <= 29.99:
        nivel = 'Acima do peso'
    elif 30 <= imc <= 34.99:
        nivel = 'Obesidade I'
    elif 35 <= imc <= 39.99:
        nivel = 'Obesidade II (severa)'
    else:
        nivel = 'Obesidade III (morbida)'

    return nivel