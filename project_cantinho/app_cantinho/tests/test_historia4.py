from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Historia3(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")

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
            #finalizando compra
            botao_comprar = self.driver.find_element(By.CLASS_NAME, 'pagamento')
            botao_comprar.click()
            time.sleep(2)
            #escolhendo metodo
            pagamento = self.driver.find_element(By.ID, 'pix')
            pagamento.click()
            pagar = self.driver.find_element(By.NAME, 'botao_pagar')
            pagar.click()
            time.sleep(2)
            try:
                codigo = self.driver.find_element(By.CLASS_NAME, 'codigo')
                assert True, codigo
            except:
                assert False

    def test_02(self):
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
            time.sleep(5)
            horario = self.driver.find_element(By.CLASS_NAME, "retirada")
            horario.send_keys('11:00')
            time.sleep(2)
            botao_salvar = self.driver.find_element(By.NAME, 'salvar_horario')
            botao_salvar.click()
            time.sleep(2)
            #finalizando compra
            botao_comprar = self.driver.find_element(By.CLASS_NAME, 'pagamento')
            botao_comprar.click()
            time.sleep(2)
            #escolhendo metodo retirada
            pagamento = self.driver.find_element(By.ID, 'pagar_retirada')
            pagamento.click()
            pagar = self.driver.find_element(By.NAME, 'botao_pagar')
            pagar.click()
            time.sleep(2)
            try:
                retirada_sucesso = self.driver.find_element(By.NAME, 'sucesso-retirada')
                assert True, retirada_sucesso
            except:
                assert False
