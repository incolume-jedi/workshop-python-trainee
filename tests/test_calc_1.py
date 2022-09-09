import pytest
from incolume.py.workshop.trainee.calc import calculadora


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    (
        (('+',3, '4'), 7),
        (('+', 3, 4), 7),
        (('-',3.0, 4), -1.0),
        (('-','3', 4), -1),
        (('*', 3, '4'), 12),
        (('*', 3, '4.0'), 12.0),
        (('/', 3, '4'), .75),
        (('/', 4, 4.0), 1.0),
        (('/', 4, 3.0), 1.3333333333333333),
        (('%', 4, 3), 1),
        (('%', 12, 7), 5),
        (('**', 3, 4), 81),
        (('**', 81, (1/4)), 3),
    )
)
def test_calculadora(entrance, expected):
    assert calculadora(*entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    (
        (('/', 3, 0), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('/', '3', 0), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('/', 3, '0'), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('/', '3', '0'), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('//', 3, 0), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('//', '3', 0), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('//', 3, '0'), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('//', '3', '0'), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('^', 3, 5), {'expected_exception': ValueError,
                       'match': r".*operador invÃ¡lido. Use: ([+\-\*\/%] ?){7} .*\."}),
        (('+', 'a', 'b'), {'expected_exception': ValueError,
                       'match': r".*x e y devem ser valores numÃ©ricos reais.*"}),
        (('+', '0', 'b'), {'expected_exception': ValueError,
                           'match': r".*x e y devem ser valores numÃ©ricos reais.*"}),
        (('+', 'a', '0'), {'expected_exception': ValueError,
                           'match': r".*x e y devem ser valores numÃ©ricos reais.*"}),
        (('+', (3 + 0j), (2 + 0j)), {'expected_exception': ValueError,
                           'match': r".*x e y devem ser valores numÃ©ricos reais.*"}),
    )
)
def test_calculadora_except(entrance, expected):
    with pytest.raises(**expected):
        calculadora(*entrance)
