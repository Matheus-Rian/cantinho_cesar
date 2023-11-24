from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Firefox()
class Historia5(LiveServerTestCase):
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

        carteira = driver.find_element(By.XPATH, "//a[@href='/adicionar_saldo/']")
        carteira.click()
        time.sleep(2)
        saldo = driver.find_element(By.XPATH, "//input[@name='valor_adicional' and @value='15']")
        saldo.click()
        adicionar = driver.find_element(By.XPATH, "//button[contains(text(),'Adicionar Saldo') and contains(@class, 'remover')]") 
        time.sleep(1)       
        adicionar.click()
        WebDriverWait(driver, 10).until(
             EC.visibility_of_element_located((By.CLASS_NAME, 'feedback'))
        )
        mensagem_sucesso = driver.find_element(By.CLASS_NAME, 'feedback').text
        self.assertIn('Valor adicionado com sucesso!', mensagem_sucesso)

        
    def test_02(self):
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

        carteira = driver.find_element(By.XPATH, "//a[@href='/adicionar_saldo/']")
        carteira.click()
        time.sleep(2)
        saldo_anterior_text = driver.find_element(By.CLASS_NAME, 'saldo-atual').text
        saldo_anterior = float(saldo_anterior_text.replace('Seu Saldo Atual: R$', '').replace(',', '').strip())
        saldo = driver.find_element(By.XPATH, "//input[@name='valor_adicional' and @value='10']")
        saldo.click()
        adicionar = driver.find_element(By.XPATH, "//button[contains(text(),'Adicionar Saldo') and contains(@class, 'remover')]") 
        time.sleep(1)       
        adicionar.click()
        WebDriverWait(driver, 10).until(
             EC.visibility_of_element_located((By.CLASS_NAME, 'feedback'))
        )
        saldo_posterior_text = driver.find_element(By.CLASS_NAME, 'saldo-atual').text
        saldo_posterior = float(saldo_posterior_text.replace('Seu Saldo Atual: R$', '').replace(',', '').strip())
        self.assertEqual(saldo_posterior, saldo_anterior + 10.00)