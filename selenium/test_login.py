from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Configuración del driver de Chrome
def setup_driver():
    """Configura y devuelve una instancia del WebDriver de Chrome."""
    chrome_options = Options()
    # Opciones para ejecución en entornos CI o sin interfaz gráfica
    # chrome_options.add_argument("--headless")  # Descomenta para modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Crear el servicio de Chrome
    # Especifica la ruta al chromedriver si es necesario
    # service = Service('/ruta/a/tu/chromedriver')
    service = Service()
    
    # Inicializar el driver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver

def test_login_saucedemo():
    """Prueba el inicio de sesión en SauceDemo y verifica el carrito de compras."""
    # Inicializar el driver
    driver = setup_driver()
    
    try:
        # Abrir la página de inicio de sesión
        driver.get("https://www.saucedemo.com/")
        
        # Esperar a que se cargue el formulario de login
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        
        # Ingresar credenciales
        username_input.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Hacer clic en el botón de login
        driver.find_element(By.ID, "login-button").click()
        
        # Verificar que el login fue exitoso comprobando que estamos en la página de productos
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        print("✅ Login exitoso!")
        
        # Añadir un producto al carrito
        driver.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]").click()
        
        # Esperar y verificar que aparezca el badge del carrito de compras
        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        
        # Verificar que el contador del carrito muestra 1
        assert badge.text == "1", f"El contador del carrito debería mostrar 1, pero muestra {badge.text}"
        print("✅ Producto añadido al carrito correctamente!")
        
        # Opcional: hacer clic en el carrito y verificar que contiene el producto
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        print("✅ Producto visible en el carrito!")
        
        # Cerrar sesión
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()
        
        # Verificar que volvimos a la página de login
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )
        print("✅ Cierre de sesión exitoso!")
        
        print("✅ ¡Todas las pruebas pasaron con éxito!")
        return True
        
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        return False
        
    finally:
        # Cerrar el navegador al finalizar
        print("Cerrando el navegador...")
        driver.quit()

if __name__ == "__main__":
    test_login_saucedemo()