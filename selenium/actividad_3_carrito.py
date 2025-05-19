"""
actividad_3_carrito.py
Añade el primer producto al carrito y verifica que está en la lista.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # Login
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # 1) Agregar al carrito el primer producto
    first_item       = driver.find_element(By.CSS_SELECTOR, ".inventory_item")
    first_item_name  = first_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    first_item.find_element(By.TAG_NAME, "button").click()   # botón “Add to cart”

    # 2) Verificar badge del carrito = 1
    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert badge == "1", f"El contador del carrito es {badge} (se esperaba 1)"

    # 3) Ir al carrito y confirmar producto
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_name = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
    assert cart_name == first_item_name, "El producto del carrito no coincide"

    print("Test OK")
finally:
    driver.quit()
