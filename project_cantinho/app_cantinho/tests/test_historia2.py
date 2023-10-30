from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Historia2(LiveServerTestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=self.options)

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
        lugar = self.driver.find_elements(By.ID, "id_Selecione_1")
        time.sleep(2)
        for botao in lugar:
            botao.click()
            time.sleep(5)
            selecionar = self.driver.find_element(By.CLASS_NAME, "custom-button")
            selecionar.click()
            time.sleep(2)
            try:
                disponivel = self.driver.find_element(By.NAME, 'produto-indisponivel')
                assert True, disponivel
            except:
                assert False