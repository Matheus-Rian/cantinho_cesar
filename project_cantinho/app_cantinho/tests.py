from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class Historia1(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_01(self):
        self.driver.get("http://127.0.0.1:8000")
        email = self.driver.find_element(By.NAME, "email")
        senha = self.driver.find_element(By.NAME, "senha")

        email.send_keys("teste25@teste.com")
        senha.send_keys("123")
        entrar = self.driver.find_element(By.XPATH, "//button[@value='Entrar']")
        time.sleep(2)
        entrar.click()
        botoes_adicionar = self.driver.find_elements(By.CLASS_NAME, "add-to-cart")   
        time.sleep(2)
        for botao in botoes_adicionar:
            botao.click()
