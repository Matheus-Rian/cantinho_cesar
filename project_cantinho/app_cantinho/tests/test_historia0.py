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
        cadastrar = self.driver.find_element(By.NAME,'botao_cadastrar')
        cadastrar.click()
        time.sleep(2)
        nome_cadastro = self.driver.find_element(By.NAME, 'nome-usuario')
        nome_cadastro.send_keys('teste01')
        time.sleep(2)
        email = self.driver.find_element(By.NAME,'email')
        email.send_keys('teste01@teste')
        time.sleep(2)
        senha = self.driver.find_element(By.NAME, 'senha')
        senha.send_keys('123')
        time.sleep(2)
        botao_cadastro = self.driver.find_element(By.CLASS_NAME, 'submit')
        botao_cadastro.click()
        time.sleep(1)

        #validacao
        try:
            product_name = self.driver.find_element(By.CLASS_NAME, 'product-name')
            assert True, product_name
        except:
            assert False