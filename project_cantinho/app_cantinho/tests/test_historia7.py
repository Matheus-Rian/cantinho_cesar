from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)
class Historia7(LiveServerTestCase):

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
        entrar.click()
        time.sleep(2)

        botao_favoritar = driver.find_element(By.XPATH, "//button[@name='botao_favoritar']")
        botao_favoritar.click()
        time.sleep(2)


        driver.get("http://127.0.0.1:8000/meus-favoritos/")

        try:
            produto_favoritado = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'favorito-info')))
            self.assertTrue(produto_favoritado.is_displayed())
        except StaleElementReferenceException:
            produto_favoritado = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'favorito-info')))
            self.assertTrue(produto_favoritado.is_displayed())