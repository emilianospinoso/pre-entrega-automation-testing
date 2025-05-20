import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import *  # Importamos todas las funciones auxiliares
import time

# Fixture para configurar y proporcionar el driver de Chrome
@pytest.fixture
def driver():
    """
    Fixture que configura y proporciona una instancia de Chrome WebDriver.
    """
    # Configuración del driver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Descomenta para modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Inicializar el driver
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    
    # Proporcionar el driver a la prueba
    yield driver
    
    # Cerrar el navegador después de cada prueba
    driver.quit()

# Test de Login con credenciales válidas
def test_login_success(driver):
    """
    Caso de prueba: Login exitoso con credenciales válidas.
    Verifica que el usuario pueda iniciar sesión y sea redirigido a la página de inventario.
    """
    # Abrir la página de login
    driver.get("https://www.saucedemo.com/")
    
    # Esperar a que el formulario de login sea visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    
    # Ingresar credenciales válidas
    username_input.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Hacer clic en el botón de login
    driver.find_element(By.ID, "login-button").click()
    
    # Verificar login exitoso comprobando la URL
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
    
    # Verificar que estamos en la página de inventario
    assert "inventory.html" in driver.current_url, "No se redirigió a la página de inventario"
    
    print("✅ Login exitoso completado")

# Test de verificación del catálogo
def test_verify_catalog(driver):
    """
    Caso de prueba: Verificación del catálogo de productos.
    Verifica que el título de la página sea correcto, que existan productos 
    y que elementos importantes de la interfaz estén presentes.
    """
    # Realizar login primero (reutilizando código)
    perform_login(driver, "standard_user", "secret_sauce")
    
    # Verificar el título de la página
    assert driver.title == "Swag Labs", f"El título de la página es incorrecto: {driver.title}"
    
    # Verificar que existan productos visibles
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    assert len(products) > 0, "No hay productos visibles en la página"
    print(f"✅ Se encontraron {len(products)} productos en el catálogo")
    
    # Verificar elementos importantes de la interfaz
    assert is_element_present(driver, By.CLASS_NAME, "product_sort_container"), "Filtro de productos no encontrado"
    assert is_element_present(driver, By.ID, "react-burger-menu-btn"), "Menú hamburguesa no encontrado"
    assert is_element_present(driver, By.CLASS_NAME, "shopping_cart_link"), "Ícono del carrito no encontrado"
    
    print("✅ Verificación del catálogo completada")

# Test de interacción con productos y carrito
def test_cart_functionality(driver):
    """
    Caso de prueba: Interacción con productos y carrito.
    Añade un producto al carrito, verifica que el contador se incremente,
    navega al carrito y comprueba que el producto añadido esté presente.
    """
    # Realizar login primero
    perform_login(driver, "standard_user", "secret_sauce")
    
    # Verificar que inicialmente no haya productos en el carrito
    assert not is_element_present(driver, By.CLASS_NAME, "shopping_cart_badge", timeout=1), "El carrito debería estar vacío inicialmente"
    
    # Obtener el nombre del primer producto para validarlo después
    product_name_element = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    product_name = product_name_element.text
    print(f"Producto seleccionado: {product_name}")
    
    # Añadir el primer producto al carrito
    add_button = driver.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]")
    add_button.click()
    
    # Verificar que el contador del carrito se incremente
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1", f"El contador del carrito debería ser 1, pero es {cart_badge.text}"
    print("✅ Producto añadido correctamente al carrito")
    
    # Navegar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Verificar que estamos en la página del carrito
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )
    
    # Verificar que el producto añadido aparezca en el carrito
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1, f"Debería haber 1 producto en el carrito, pero hay {len(cart_items)}"
    
    # Verificar que sea el mismo producto que añadimos
    cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item_name == product_name, f"El producto en el carrito ({cart_item_name}) no coincide con el añadido ({product_name})"
    
    print("✅ Verificación del carrito completada")

# Test adicional (opcional): Login con credenciales inválidas
def test_login_invalid_credentials(driver):
    """
    Caso de prueba (opcional): Login con credenciales inválidas.
    Verifica que se muestre un mensaje de error apropiado.
    """
    # Abrir la página de login
    driver.get("https://www.saucedemo.com/")
    
    # Esperar a que el formulario de login sea visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    
    # Ingresar credenciales inválidas
    username_input.send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    
    # Hacer clic en el botón de login
    driver.find_element(By.ID, "login-button").click()
    
    # Verificar que aparezca un mensaje de error
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    
    assert "Username and password do not match" in error_message.text, "El mensaje de error no es el esperado"
    print("✅ Prueba de credenciales inválidas completada")

# Test adicional (opcional): Cierre de sesión
def test_logout(driver):
    """
    Caso de prueba (opcional): Cierre de sesión.
    Verifica que el usuario pueda cerrar sesión correctamente.
    """
    # Realizar login primero
    perform_login(driver, "standard_user", "secret_sauce")
    
    # Abrir el menú
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    
    # Esperar a que el botón de logout sea clickeable
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    
    # Hacer clic en logout
    logout_link.click()
    
    # Verificar que volvimos a la página de login
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    
    assert driver.current_url == "https://www.saucedemo.com/", "No se redirigió a la página de login después de cerrar sesión"
    print("✅ Cierre de sesión completado")