import allure
from src.calcular_numeros import calcular_promedio


@allure.description("Test para calcular promedio")
@allure.feature("Calcular promedio")
@allure.epic("")
def test_calcular_promedio():
    numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(numeros)
    assert promedio == 3
