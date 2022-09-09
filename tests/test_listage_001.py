import pytest
from incolume.py.workshop.trainee import listage_001
from math import pi


@pytest.mark.parametrize(
    'entrance',
    [f'ex{x:02}' for x in range(1, 19)]
)
def test_exercices(entrance):
    assert entrance in dir(listage_001)


@pytest.mark.parametrize(
    'entrance params expected'.split(),
    (
        (listage_001.ex01, (), 'Alô mundo'),
        (listage_001.ex02, (3,), 'O número informado foi 3'),
        (listage_001.ex03, (3, 4), 'Soma: 7'),
        (listage_001.ex04, (3, 4, 7, 6), 'Média: 5.0'),
        (listage_001.ex05, (10,), '10m equivale a 1000cm'),
        (
            listage_001.ex06,
            (5, ),
            f'Circulo de raio 5, '
            f'possui perimetro {2*pi*5:.2} e área {pi*5**2:.2}'
        ),
        (listage_001.ex07, (5, ), 'dobro da área: 50m2'),
        (listage_001.ex08, (40, 100), 'Salário do mês R$4.000,00'),
        (listage_001.ex09, (), ''),
        (listage_001.ex10, (), ''),
        (listage_001.ex11, (), ''),
        (listage_001.ex12, (), ''),
        (listage_001.ex13, (), ''),
        (listage_001.ex14, (), ''),
        (listage_001.ex15, (), ''),
        (listage_001.ex16, (), ''),
        (listage_001.ex17, (), ''),
        (listage_001.ex18, (), ''),

    ),
)
def test_screen(capsys, entrance, params, expected):
    entrance(*params)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
