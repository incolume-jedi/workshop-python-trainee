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
            (5,),
            f'Circulo de raio 5, '
            f'possui perimetro {2 * pi * 5:.2} e área {pi * 5 ** 2:.2}'
        ),
        (listage_001.ex07, (5,), 'dobro da área: 50m2'),
        (listage_001.ex08, (40.05, 110), 'Salário do mês: R$ 4,405.50'),
        (listage_001.ex09, (1,), '1.00º F equivale(m) a -17.22º C'),
        (listage_001.ex09, (82.5,), '82.50º F equivale(m) a 28.06º C'),
        (listage_001.ex10, (-17.22,), '-17.22º C equivale(m) a 1.00º F'),
        (listage_001.ex11, (2, 4, 5.), '8.0, 11.0 e 125.0'),
        (listage_001.ex12, (1.78,), 'peso ideal: 71.41'),
        (listage_001.ex13, (1.78, 'm'), 'peso ideal: 71.41'),
        (listage_001.ex13, (1.78, 'f'), 'peso ideal: 65.84'),
        (listage_001.ex14, (10,), 'Peso: 10Kg \nLimite: 50.0 '
                                  '\nExcesso: 0 Kg \nMulta: R$ 0.0'),
        (listage_001.ex14, (60,), 'Peso: 60Kg \nLimite: 50.0 '
                                  '\nExcesso: 10.0 Kg \nMulta: R$ 40.0'),
        (listage_001.ex15, (10, 10), '+ Salário Bruto    R$ 100.00\n'
                                     '- IR (11%)         R$ 11.00\n'
                                     '- INSS (8%)        R$ 8.00\n'
                                     '- Sindicato ( 5%)  R$ 5.00\n'
                                     '= Salário Líquido  R$ 76.00'),
        (listage_001.ex16, (180,), 'Metragem: 180.00 m2,'
                                   '\nvolume necessário: 60.0 L,'
                                   '\nLatas necessárias: 4 (~3.33), '
                                   '\nValor: R$ 320.00'),
        (listage_001.ex17, (360,), 'Metragem: 360.00 m2,'
                                   '\nvolume necessário: 60.0 L,'
                                   '\nLatas necessárias: 4 (~3.33), '
                                   '\nValor: R$ 320.00,'
                                   '\nGalões necessários: 17 (~16.67), '
                                   '\nValor: R$ 425.00'
                                   '\nLatas 3.0(54.0L) + Galoes 4(14.4L),'
                                   '\nValor: R$ 340.00'),
        (
            listage_001.ex18, (5000, 500),
            'Tempo estimado de download:  0.17 min'
        ),

    ),
)
def test_screen(capsys, entrance, params, expected):
    entrance(*params)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
