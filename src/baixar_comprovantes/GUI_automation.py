import inspect
import time
import traceback

import pywinauto
from pywinauto import keyboard
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.reg_log import log_info, log_warning
from src.webdriver_manager import DriverManagerChrome


def verif_incluir_anexo(browser):
    erro = None
    contador = 0
    while contador < 3:
        try:
            browser.implicitly_wait(5)
            elemento = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[5]/td/a')
            ))
            return True
        except Exception as e:
            log_warning(f'Erro ao VERIFICAR "Incluir anexo"...\n{e}')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    log_warning('Erro ao VERIFICAR  "Incluir anexo"...', erro)
    return False

def click_incluir_anexo(browser):
    erro = None
    contador = 0
    while contador < 3:
        try:
            browser.implicitly_wait(5)
            elemento = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[5]/td/a')
            ))

            elemento.click()
            return True
        except Exception as e:
            log_warning(f'Erro ao CLICAR "Incluir anexo"...\n{e}')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    log_warning('Erro ao clicar em "Incluir anexo"...', erro)
    return False

def input_num_processo_comprovante(browser, n_processo):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH,
                                            '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/input[1]')
            elemento.send_keys(n_processo)
            return
        except Exception as e:
            log_warning('Erro ao clicar em "Input número processo"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_btn_pesquisar_comprovante(browser):
    erro = None
    contador = 0
    while contador < 15:
        try:
            browser.implicitly_wait(1)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/input[2]')
            time.sleep(1)
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "Pesquisar"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')



def click_btn_duas_setas_direita(browser):
    erro = None
    contador = 0
    while contador < 2:
        try:
            browser.implicitly_wait(3)
            linhas = browser.find_elements(By.XPATH, '//*[@id="oTable"]/tbody/tr')
            linha = linhas[-1]
            setas = linha.find_elements(By.XPATH, f'./td/a')
            seta = setas[-1]
            elemento = seta.find_element(By.XPATH, f'./img')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "duas setas direita"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_btn_uma_seta_esquerda(browser):
    erro = None
    contador = 0
    while contador < 3:
        try:
            browser.implicitly_wait(3)
            linhas = browser.find_elements(By.XPATH, '//*[@id="oTable"]/tbody/tr')
            linha = linhas[-1]
            setas = linha.find_elements(By.XPATH, f'./td/a')
            seta = setas[1]
            elemento = seta.find_element(By.XPATH, f'./img')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "uma seta esquerda"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def find_table(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            linhas = browser.find_elements(By.XPATH, '//*[@id="oTable"]/tbody/tr')
            return linhas
        except Exception as e:
            log_warning('Erro ao encontrar tabela...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


def click_visualizar_arq(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '//*[@id="visualizar"]')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "Visualizar arquivo"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_x_comprovante(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '//*[@id="pop"]/table/tbody/tr[1]/td/a')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "x"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_btn_voltar(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH,
                                            '//*[@id="btoVoltar"]')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "Voltar"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

