import pytest
from conversores_temp import converter_temperatura


# --- [ Testes de Caminho Feliz (Happy Path) ] --- #

@pytest.mark.happy_path
@pytest.mark.parametrize(
    "de_temperatura, para_temperatura, valor, resultado_esperado",
    [
        # Caso 1: Kelvin para Celsius
        ("KELVIN", "CELSIUS", 50,       -223.15),
        # Caso 2: Kelvin para Fahrenheit
        ("KELVIN", "FAHRENHEIT", 50,    -369.67),

        # Caso 3: Celsius para Kelvin
        ("CELSIUS", "KELVIN", 50,       323.15),
        # Caso 4: Celsius para Fahrenheit
        ("CELSIUS", "FAHRENHEIT", 50,   122),

        # Caso 5: Fahrenheit para Celsius
        ("FAHRENHEIT", "CELSIUS", 50,   10),
        # Caso 6: Fahrenheit para Kelvin
        ("FAHRENHEIT", "KELVIN", 50,   283.15),
    ],
    ids = ["kelvin_celsius", "kelvin_fahrenheit", "celsius_kelvin", "celsius_fahrenheit", "fahrenheit_celsius", "fahrenheit_kelvin"]
)
def test_converter_temperatura_validos(de_temperatura, para_temperatura, valor, resultado_esperado):
    resultado = converter_temperatura(de_temperatura, para_temperatura, valor)

    assert resultado == pytest.approx(resultado_esperado)