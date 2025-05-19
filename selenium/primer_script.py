from selenium import webdriver          #Importamos la librería que permite controlar el navegador
import time                             #Para hacer pausas visibles (solo demo)

driver = webdriver.Chrome()             #Creamos la instancia del driver → abre una ventana de Chrome vacía

try:
    driver.get('https://www.saucedemo.com')  #Navegamos a la URL de Sauce Demo (pantalla de login)

    print('Título:', driver.title)      #Leemos el título de la pestaña → debería salir "Swag Labs"
    assert driver.title == 'Swag Labs'  #Validamos que el título sea el esperado (asegura que cargó bien)

    time.sleep(2)                       #Pausa de 2 s para que lo veas (luego la quitaremos)
finally:
    driver.quit()                       #Cierre limpio: mata la sesión y la ventana
