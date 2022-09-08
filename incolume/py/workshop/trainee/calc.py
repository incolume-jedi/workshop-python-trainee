__author__ = '@britodfbr'
from pathlib import Path

project = Path(__file__).parents[4]


def calculadora():
    """Realiza uma operação matemática.

    :param op: operador (str),
    :param x: valor numérico (float|int|str)
    :param y: valor numérico (float|int|str)
    :return: retorna um valor numérico (float)
    """
    result = 0
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile(
        project.joinpath("tests", "test_calc.txt").as_posix(),
        module_relative=False
    )
