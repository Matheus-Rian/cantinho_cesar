# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from time import sleep

# chrome_options = webdriver.ChromeOptions()
# chrome_browser = webdriver.Chrome(options=chrome_options)

# class teste1(LiveServerTestCase):
#         chrome_browser.get('http://127.0.0.1:8000/')
#         email = chrome_browser.find_element(By.NAME, "email")
#         senha = chrome_browser.find_element(By.NAME, "senha")
#         email.send_keys("teste25@teste.com")
#         senha.send_keys("123")
#         entrar = chrome_browser.find_element(By.XPATH, "//button[@value='Entrar']")
#         sleep(2)
#         entrar.click()
#         sleep(2)
#         botoes_adicionar = chrome_browser.find_elements(By.CLASS_NAME, "add-to-cart")
#         sleep(2)
#         for botao in botoes_adicionar:
#             botao.click()
#             sleep(2)
#         horario = chrome_browser.find_element(By.NAME, 'hora_retirada2')
#         horario.send_keys('11:00')
#         sleep(4)
#         botao_salvar = chrome_browser.find_element(By.NAME, 'salvar_horario')
#         botao_salvar.click()
#         sleep(6)

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Historia3(LiveServerTestCase):
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
            time.sleep(5)
            horario = self.driver.find_element(By.CLASS_NAME, "retirada")
            horario.send_keys('11:00')
            time.sleep(2)
            botao_salvar = self.driver.find_element(By.NAME, 'salvar_horario')
            botao_salvar.click()
            time.sleep(2)