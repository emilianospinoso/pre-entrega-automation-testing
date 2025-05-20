import pytest
import os
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# Crear directorio para capturas de pantalla si no existe
def pytest_configure(config):
    """
    Configuración que se ejecuta al iniciar pytest.
    Crea el directorio para capturas de pantalla si no existe.
    """
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
        print("Directorio 'screenshots' creado.")

# Hook para tomar capturas de pantalla cuando un test falla
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que captura screenshots cuando un test falla.
    """
    # Ejecutar todas las demás hooks para obtener el resultado
    outcome = yield
    rep = outcome.get_result()
    
    # Verificamos si estamos en la fase de call y si ha fallado el test
    if rep.when == "call" and rep.failed:
        # Intentamos obtener el driver desde la fixture
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"failure_{item.name}_{timestamp}.png"
            driver.save_screenshot(f"screenshots/{screenshot_name}")
            print(f"\nCaptura de pantalla guardada: {screenshot_name}")