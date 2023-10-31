from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)
class Historia2(LiveServerTestCase):
# Create your tests here.
    def test_01(self):
        driver.get("http://127.0.0.1:8000")
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        senha = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "senha"))
        )

        email.send_keys("teste25@teste.com")
        senha.send_keys("123")
        entrar = driver.find_element(By.XPATH, "//button[@value='Entrar']")
        time.sleep(2)
        entrar.click()
        lugar = driver.find_elements(By.ID, "id_Selecione_1")
        time.sleep(2)
        for botao in lugar:
            botao.click()
            time.sleep(5)
            selecionar = driver.find_element(By.CLASS_NAME, "custom-button")
            selecionar.click()
            time.sleep(2)