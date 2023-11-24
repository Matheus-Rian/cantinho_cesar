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

        email.send_keys("vendedor@gmail.com")
        senha.send_keys("1234")

        entrar = driver.find_element(By.XPATH, "//button[@value='Entrar']")
        time.sleep(2)
        entrar.click()
        time.sleep(10)

        sair = driver.find_element(By.CLASS_NAME, 'btn-sair')
        sair.click()
        time.sleep(2)

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
        time.sleep(10)

        botoes_adicionar = driver.find_elements(By.XPATH, "//a[contains(@class, 'add-to-cart') and text()='Adicionar ao carrinho']")
        time.sleep(2)

        for botao in botoes_adicionar:
            try:
                botao.click()
                time.sleep(5)
                horario = driver.find_element(By.CLASS_NAME, "retirada")
                horario.send_keys('11:00')
                time.sleep(2)
                botao_salvar = driver.find_element(By.NAME, 'salvar_horario')
                botao_salvar.click()
                time.sleep(2)
                botao_comprar = driver.find_element(By.CLASS_NAME, 'pagamento')
                botao_comprar.click()
                time.sleep(2)
                pagamento = driver.find_element(By.ID, 'pix')
                pagamento.click()
                pagar = driver.find_element(By.NAME, 'botao_pagar')
                pagar.click()
                time.sleep(2)
                try:
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'codigo')))
                except NoSuchElementException:
                    self.fail("Elemento 'código' não foi encontrado após o pagamento com pix.")
            except StaleElementReferenceException:
                continue

        seta = driver.find_element(By.CLASS_NAME, 'img-seta')
        seta.click()
        time.sleep(2)
        sair = driver.find_element(By.CLASS_NAME, 'btn-sair')
        sair.click()
        time.sleep(2)

        try:
            email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
            senha = driver.find_element(By.CSS_SELECTOR, "input[name='senha']")
        except NoSuchElementException:
            print("Email or senha element not found.")
            return

        email.send_keys("vendedor@gmail.com")
        senha.send_keys("1234")

        entrar = driver.find_element(By.XPATH, "//button[@value='Entrar']")
        time.sleep(2)
        entrar.click()
        time.sleep(10)