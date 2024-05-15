from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

# Configurando o Selenium
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Acessando a página
driver.get('https://www.vilarica.com.br/comprar/prontos/sao-leopoldo-rs')

# Aguardando o carregamento da página
driver.implicitly_wait(10)  # Aguarda até 10 segundos pelo carregamento dos elementos

# Criando uma pasta para armazenar os screenshots
os.makedirs('screenshots', exist_ok=True)

# Tentando encontrar todos os elementos com a classe 'wrap-link'
anuncios = driver.find_elements(By.CLASS_NAME, 'wrap-link')

# Iterando sobre os elementos encontrados e extraindo informações
for i, anuncio in enumerate(anuncios):
    url = anuncio.get_attribute('href')
    try:
        titulo = anuncio.find_element(By.XPATH, ".//p[@class='property-title']").text
    except:
        titulo = "Título não encontrado"
    try:
        preco = anuncio.find_element(By.XPATH, ".//p[@class='price']").text
    except:
        preco = "Preço não encontrado"

    print(f"URL: {url}")
    print(f"Título: {titulo}")
    print(f"Preço: {preco}")
    print("-" * 50)

    # Capturando o screenshot do elemento
    screenshot_path = f'screenshots/anuncio_{i + 1}.png'
    anuncio.screenshot(screenshot_path)
    print(f"Screenshot salvo em: {screenshot_path}")

# Fechando o navegador
driver.quit()
