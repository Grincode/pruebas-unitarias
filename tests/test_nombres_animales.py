import allure
from src.animales import obtener_nombres_animales


@allure.description("Test para obtener nombres de animales")
@allure.feature("Animales")
@allure.epic("")
def test_obtener_nombres():
    nombres = obtener_nombres_animales()
    assert isinstance(nombres, list)
