"""
actividad_1_login.py
Automatiza el login en Sauce Demo y valida la URL y el título.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1) Crear el driver (Chrome por defecto)
driver = webdriver.Chrome()
driver.implicitly_wait(5)          # espera implícita para todos los find_element

try:
    # 2) Abrir la pantalla de login
    driver.get("https://www.saucedemo.com")

    # 3) Completar usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 4) Enviar formulario
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # 5) Verificar redirección a /inventory.html
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

    # — Reto extra —
    assert driver.title == "Swag Labs", "Título inesperado"

    print("Test OK")
finally:
    # 6) Cerrar el navegador
    driver.quit()
