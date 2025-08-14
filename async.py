# Importa la API asíncrona de Playwright
import asyncio
from playwright.async_api import async_playwright

# Definimos la función principal asíncrona
async def main():
    # Inicia Playwright en modo asíncrono
    async with async_playwright() as p:
        # Lanza el navegador Firefox en modo visible (headless=False)
        browser = await p.firefox.launch(headless=False)
        # Crea una nueva pestaña/página
        page = await browser.new_page()
        # Navega a la URL indicada
        await page.goto("https://whatmyuseragent.com/")
        # Imprime el título de la página en la consola
        print(await page.title())
        # Cierra el navegador
        await browser.close()

# Ejecuta la función principal asíncrona
asyncio.run(main())
