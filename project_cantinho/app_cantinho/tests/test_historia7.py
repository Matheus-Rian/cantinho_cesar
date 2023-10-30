from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Historia7(LiveServerTestCase):
    def __init__(self):
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
        botoes_adicionar_favorito = self.driver.find_elements(By.NAME, "botao_favoritar")
        for botao in botoes_adicionar_favorito:
            botao.click()
            time.sleep(8)
            #acessando favoritos
            favoritos = self.driver.find_element(By.NAME, "meus_favoritos")
            favoritos.click()
            time.sleep(5)
            try:
                favoritos_sucesso = self.driver.find_element(By.CLASS_NAME, 'favorito-info')
                assert True, favoritos_sucesso
            except:
                assert False