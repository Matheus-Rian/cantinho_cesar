from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

class Historia1(LiveServerTestCase):
    def test_01(self):
        driver.get("http://127.0.0.1:8000")
        try:
            email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
            senha = driver.find_element(By.CSS_SELECTOR, "input[name='senha']")
        except NoSuchElementException:
            print("Email or senha element not found.")
            return

        email.send_keys("teste25@teste.com")
        senha.send_keys("123")

        entrar = driver.find_element(By.XPATH, "//button[@value='Entrar']")
        time.sleep(2)
        entrar.click()

        botoes_adicionar = driver.find_elements(By.XPATH, "//a[contains(@class, 'add-to-cart') and text()='Adicionar ao carrinho']")
        time.sleep(2)
        quant_testes = 3 
        for botao in botoes_adicionar:
            testes = 0
            while testes < quant_testes:
                
                try:
                    botao.click()
                    break 
                except StaleElementReferenceException:
                    print("Stale Element Reference. Retrying...")
                    botoes_adicionar = driver.find_elements(By.XPATH, "//a[contains(@class, 'add-to-cart') and text()='Adicionar ao carrinho']")

                except TimeoutException:
                    print("TimeoutException. Botão não encontrado.")
                    break 
                testes+=1