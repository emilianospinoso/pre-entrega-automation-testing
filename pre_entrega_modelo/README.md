Pre-entrega Proyecto Final - Automatización de Testing
Este proyecto implementa una automatización de pruebas para el sitio SauceDemo, utilizando Selenium WebDriver y Python.
Propósito del Proyecto
El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo:

Login con credenciales válidas e inválidas
Verificación del catálogo de productos
Interacción con el carrito de compras (añadir productos y verificar su contenido)
Cierre de sesión

Tecnologías Utilizadas

Python: Lenguaje de programación principal
Pytest: Framework de testing para estructurar y ejecutar pruebas
Selenium WebDriver: Para la automatización de la interfaz web
Git/GitHub: Para control de versiones y compartir el código

Estructura del Proyecto
pre_entrega_modelo/
├── conftest.py # Configuraciones adicionales para pytest
├── helpers.py # Funciones auxiliares reutilizables
├── test_saucedemo.py # Casos de prueba automatizados
└── screenshots/ # Directorio para capturas de pantalla (se crea automáticamente)
Instalación de Dependencias

Asegúrate de tener Python 3.7 o superior instalado
Instala las dependencias necesarias:

pip install selenium pytest pytest-html

Descarga el WebDriver correspondiente a tu navegador:

ChromeDriver
GeckoDriver (Firefox)

Asegúrate de que el WebDriver esté en tu PATH o especifica su ubicación en el código

Ejecución de las Pruebas
Para ejecutar todas las pruebas:
python3 -m pytest pre_entrega_modelo/test_saucedemo.py -v

Para generar un reporte HTML:
python3 -m pytest pre_entrega_modelo/test_saucedemo.py -v --html=reporte.html

Funcionalidades Implementadas

1. Automatización de Login

Caso de éxito con credenciales válidas
Caso de fallo con credenciales inválidas

2. Verificación del Catálogo

Comprobación del título de la página
Verificación de presencia de productos
Validación de elementos de la interfaz (menú, filtros, etc.)

3. Interacción con el Carrito

Añadir producto al carrito
Verificar que el contador se incremente
Navegar al carrito
Comprobar que el producto añadido aparezca correctamente

4. Cierre de Sesión

Verificar que el usuario pueda cerrar sesión correctamente

Características Adicionales

Capturas de pantalla automáticas: Se toman capturas de pantalla cuando un test falla
Funciones auxiliares reutilizables: En el archivo helpers.py

Autor
[Tu Nombre]
Notas

Este proyecto fue desarrollado como pre-entrega para el curso de Automatización de Testing.
Todas las pruebas están diseñadas para funcionar con el sitio web SauceDemo en su versión actual.
