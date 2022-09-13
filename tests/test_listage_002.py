import pytest
from incolume.py.workshop.trainee import listage_002
from math import pi


@pytest.mark.parametrize(
    'entrance',
    [f'ex{x:02}' for x in range(1, 15)]
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
        (listage_002.ex09, (), ''),
        (listage_002.ex10, (), ''),
        (listage_002.ex11, (), ''),
        (listage_002.ex12, (), ''),
        (listage_002.ex13, (), ''),
        (listage_002.ex14, (), ''),
    ),
)
def test_screen(capsys, entrance, params, expected):
    entrance(*params)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
