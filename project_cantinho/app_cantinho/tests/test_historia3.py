from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-path=/path/to/chromedriver.log")
driver = webdriver.Chrome(options=options)

class Historia3(LiveServerTestCase):
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

        while True:
            try:
                botao_adicionar = driver.find_element(By.XPATH, "//a[contains(@class, 'add-to-cart') and text()='Adicionar ao carrinho']")
                botao_adicionar.click()
                time.sleep(5)

                horario = driver.find_element(By.CLASS_NAME, "retirada")
                horario.send_keys('11:00')
                time.sleep(2)

                botao_salvar = driver.find_element(By.NAME, 'salvar_horario')
                botao_salvar.click()
                time.sleep(2)

                try:
                    horario = driver.find_element(By.CLASS_NAME, "retirada")
                except NoSuchElementException:
                    sucesso = driver.find_element(By.CLASS_NAME, 'success')
                    self.assertIsNotNone(sucesso, "Element 'success' not found")
                    warning = driver.find_element(By.CLASS_NAME, 'warning')
                    self.assertIsNotNone(warning, "Element 'warning' not found")


            except:
                break