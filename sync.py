# Importación de Playwright (modo síncrono)
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Lanzar navegador Chromium (False = modo visible)
    browser = p.chromium.launch(headless=False)
    # Crear nueva pestaña
    page = browser.new_page()
    # Ir a la página que queremos scrapear
    page.goto('https://whatmyuseragent.com/')
    # Capturar pantalla y guardar como demo.png
    page.screenshot(path='demo.png')
    # Cerrar navegador
    browser.close()




