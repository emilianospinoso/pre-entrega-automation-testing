from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def is_element_present(driver, by, value, timeout=10):
    """
    Verifica si un elemento está presente en la página.
    
    Args:
        driver: Instancia del WebDriver
        by: Tipo de localizador (By.ID, By.CSS_SELECTOR, etc.)
        value: Valor del localizador
        timeout: Tiempo máximo de espera (segundos)
        
    Returns:
        bool: True si el elemento está presente, False en caso contrario
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except TimeoutException:
        return False

def is_element_visible(driver, by, value, timeout=10):
    """
    Verifica si un elemento está visible en la página.
    
    Args:
        driver: Instancia del WebDriver
        by: Tipo de localizador (By.ID, By.CSS_SELECTOR, etc.)
        value: Valor del localizador
        timeout: Tiempo máximo de espera (segundos)
        
    Returns:
        bool: True si el elemento está visible, False en caso contrario
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        return True
    except TimeoutException:
        return False

def perform_login(driver, username, password):
    """
    Realiza el inicio de sesión en SauceDemo.
    
    Args:
        driver: Instancia del WebDriver
        username: Nombre de usuario
        password: Contraseña
    """
    from selenium.webdriver.common.by import By
    
    # Abrir la página de login
    driver.get("https://www.saucedemo.com/")
    
    # Esperar a que el formulario de login sea visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    
    # Ingresar credenciales
    username_input.send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    
    # Hacer clic en el botón de login
    driver.find_element(By.ID, "login-button").click()
    
    # Esperar a que se complete el login
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

def add_product_to_cart(driver, product_index=0):
    """
    Añade un producto específico al carrito.
    
    Args:
        driver: Instancia del WebDriver
        product_index: Índice del producto a añadir (por defecto, el primero)
        
    Returns:
        str: Nombre del producto añadido
    """
    from selenium.webdriver.common.by import By
    
    # Obtener todos los productos
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    if product_index >= len(products):
        raise IndexError(f"Índice de producto {product_index} fuera de rango (hay {len(products)} productos)")
    
    # Obtener el producto específico
    product = products[product_index]
    
    # Obtener el nombre del producto
    product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    # Añadir al carrito
    add_button = product.find_element(By.XPATH, ".//button[contains(@data-test, 'add-to-cart')]")
    add_button.click()
    
    return product_name

def get_cart_count(driver):
    """
    Obtiene el número de productos en el carrito.
    
    Args:
        driver: Instancia del WebDriver
        
    Returns:
        int: Número de productos en el carrito, 0 si está vacío
    """
    from selenium.webdriver.common.by import By
    
    try:
        badge = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return int(badge.text)
    except TimeoutException:
        # Si no hay badge, el carrito está vacío
        return 0

def take_screenshot(driver, filename):
    """
    Toma una captura de pantalla y la guarda.
    
    Args:
        driver: Instancia del WebDriver
        filename: Nombre del archivo donde guardar la captura
    """
    try:
        driver.save_screenshot(f"screenshots/{filename}")
        print(f"Captura de pantalla guardada como {filename}")
    except Exception as e:
        print(f"Error al guardar la captura de pantalla: {e}")