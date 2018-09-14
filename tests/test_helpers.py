from coffee_shop.helpers import verificaNivel,calculaIMC


def test_verificaNivel():
    assert verificaNivel(16) == 'Muito abaixo do peso'
    assert verificaNivel(17) == 'Abaixo do peso'
    assert verificaNivel(19) == 'Peso normal'
    assert verificaNivel(25) == 'Acima do peso'
    assert verificaNivel(30) == 'Obesidade I'
    assert verificaNivel(35) == 'Obesidade II (severa)'
    assert verificaNivel(40) == 'Obesidade III (morbida)'