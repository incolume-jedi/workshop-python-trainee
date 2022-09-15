from pathlib import Path

import pytest
from incolume.py.workshop.trainee import listage_002
from math import pi


@pytest.mark.parametrize(
    'entrance',
    [f'ex{x:02}' for x in range(1, 13)]
)
def test_exercices(entrance):
    assert entrance in dir(listage_002)


@pytest.mark.parametrize(
    'entrance params expected'.split(),
    (
        (
            listage_002.ex01,
            ('Jesus', 'JESUS'),
            'Comparação de strings'
            '\nString 1: Jesus'
            '\nString 2: JESUS'
            '\nTamanho de "Jesus": 5'
            '\nTamanho de "JESUS": 5'
            '\nAs duas strings são de tamanhos iguais'
            '\nAs duas strings são de conteúdos diferentes'
        ),
        (
            listage_002.ex01,
            ('jesus', 'jesus'),
            'Comparação de strings'
            '\nString 1: jesus'
            '\nString 2: jesus'
            '\nTamanho de "jesus": 5'
            '\nTamanho de "jesus": 5'
            '\nAs duas strings são de tamanhos iguais'
            '\nAs duas strings são de conteúdos iguais'
        ),
        (listage_002.ex02, ('Jesus', ), 'SUSEJ'),
        (listage_002.ex03, ('Jesus', ), 'J\ne\ns\nu\ns'),
        (listage_002.ex04, ('Jesus', ),  'J\nJe\nJes\nJesu\nJesus'),
        (listage_002.ex05, ('Jesus', ), 'Jesus\nJesu\nJes\nJe\nJ'),
        (listage_002.ex06, ('20/06/1978',), 'Você nasceu em 20 de junho de 1978.'),
        (listage_002.ex07, ('Jesus te ama!',), 'espaços: 2, vogais: 5.'),
        (listage_002.ex08, ('osso', ), 'True'),
        (listage_002.ex08, ('ovo', ), 'True'),
        (listage_002.ex08, ('subi no onibus', ), 'True'),
        (listage_002.ex08, ('casa', ), 'False'),
        (listage_002.ex09, ('000.000.000-00',), 'Inválido'),
        (listage_002.ex09, ('000.000.001-91',), 'Válido'),
        (listage_002.ex10, (10,), 'dez'),
        (listage_002.ex10, (11,), 'onze'),
        (listage_002.ex10, (19,), 'dezenove'),
        (listage_002.ex10, (99,), 'noventa e nove'),
        (listage_002.ex10, (0,), 'zero'),
        (listage_002.ex10, (25,), 'vinte e cinco'),
        (listage_002.ex10, (52,), 'cinquenta e dois'),
        (listage_002.ex10, (38,), 'trinta e oito'),
        (listage_002.ex10, (47,), 'quarenta e sete'),
        (listage_002.ex10, (0,), 'zero'),
        (listage_002.ex10, (100,), 'Somente números entre 0 e 99.'),
        (listage_002.ex10, (-1,), 'Somente números entre 0 e 99.'),
        (listage_002.ex11, ('345-1234',), '3345-1234'),
        (listage_002.ex11, ('3451234',), '3345-1234'),
        (listage_002.ex11, ('4610133',), '3461-0133'),
        (listage_002.ex11, ('461-0133',), '3461-0133'),
        (listage_002.ex11, ('34610133',), '3461-0133'),
        (listage_002.ex12, ('leet', ), 'l33t'),
        (listage_002.ex12, ('casa',), '<@$@'),
        (listage_002.ex12, ('bola',), 'b0l@'),
    ),
)
def test_screen(capsys, entrance, params, expected):
    entrance(*params)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
