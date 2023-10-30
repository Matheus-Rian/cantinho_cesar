from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Historia1(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

# Create your tests here.
    def test_01(self):
        self.driver.get("http://127.0.0.1:8000")
        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        senha = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "senha"))
        )

        email.send_keys("teste25@teste.com")
        senha.send_keys("123")
        entrar = self.driver.find_element(By.XPATH, "//button[@value='Entrar']")
        time.sleep(2)
        entrar.click()
        botoes_adicionar = self.driver.find_elements(By.CLASS_NAME, "add-to-cart")
        time.sleep(2)
        for botao in botoes_adicionar:
            botao.click()
            time.sleep(2)