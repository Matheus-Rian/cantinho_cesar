from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_browser = webdriver.Chrome(options=chrome_options)

class teste1(LiveServerTestCase):
        chrome_browser.get('http://127.0.0.1:8000/')
        email = chrome_browser.find_element(By.NAME, "email")
        senha = chrome_browser.find_element(By.NAME, "senha")
        email.send_keys("teste25@teste.com")
        senha.send_keys("123")
        entrar = chrome_browser.find_element(By.XPATH, "//button[@value='Entrar']")
        sleep(2)
        entrar.click()
        sleep(2)
        lugar = chrome_browser.find_element(By.ID, "id_Selecione_1")
        sleep(2)
        lugar.click()
        sleep(2)
        selecionar = chrome_browser.find_element(By.CLASS_NAME, "custom-button")
        selecionar.click()
        sleep(2)


