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


def press_f12():
    keyboard.send_keys('{F12}')
    return

def escrever(palavra):
    keyboard.send_keys(palavra)
    return

def verificar_menu(resolucao):
    erro = None
    contador = 0
    while contador <= 10:
        try:
            print(fr'.\public\{resolucao}\menu_principal.png')
            img = pyautogui.locateOnScreen(
                fr'.\public\{resolucao}\menu_principal.png')
            time.sleep(0.5)
            pywinauto.mouse.click(button='left', coords=((img[0] + 15), (img[1] + 30)))
            time.sleep(1)
            log_info(f'coord btn ok= {img[0]}, {img[1]}')
            return
        except Exception as e:
            log_warning(f'Houve um erro na funcão {inspect.currentframe().f_code.co_name}, aguarde...')
            contador += 1
            time.sleep(2)
            erro = traceback.format_exc()

    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_setas_dev_tools(resolucao):
    erro = None
    contador = 0
    while contador <= 10:
        try:
            img = pyautogui.locateOnScreen(
                fr'.\public\{resolucao}\setas_dev_tools.png')
            time.sleep(0.5)
            pywinauto.mouse.click(button='left', coords=((img[0]+25), (img[1])))
            time.sleep(1)
            log_info(f'coord btn ok= {img[0]}, {img[1]}')
            return
        except Exception as e:
            log_warning(f'Houve um erro na funcão {inspect.currentframe().f_code.co_name}, aguarde...')
            contador += 1
            time.sleep(0.5)
            erro = traceback.format_exc()

    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_btn_application(resolucao):
    erro = None
    contador = 0
    while contador <= 10:
        try:
            img = pyautogui.locateOnScreen(
                fr'.\public\{resolucao}\btn_application.png')
            time.sleep(0.5)
            pywinauto.mouse.click(button='left', coords=((img[0]), (img[1])))
            time.sleep(1)
            log_info(f'coord btn ok= {img[0]}, {img[1]}')
            return
        except Exception as e:
            log_warning(f'Houve um erro na funcão {inspect.currentframe().f_code.co_name}, aguarde...')
            contador += 1
            time.sleep(0.5)
            erro = traceback.format_exc()

    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_btn_cookies(resolucao):
    erro = None
    contador = 0
    while contador <= 10:
        try:
            img = pyautogui.locateOnScreen(
                fr'.\public\{resolucao}\btn_cookies.png')
            time.sleep(0.5)
            pywinauto.mouse.double_click(button='left', coords=((img[0]), (img[1]+15)))
            time.sleep(0.5)
            pywinauto.mouse.click(button='left', coords=((img[0]+25), (img[1] + 35)))
            log_info(f'coord btn ok= {img[0]}, {img[1]}')
            return
        except Exception as e:
            log_warning(f'Houve um erro na funcão {inspect.currentframe().f_code.co_name}, aguarde...')
            contador += 1
            time.sleep(0.5)
            erro = traceback.format_exc()

    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


def click_input_filter(resolucao, img=None):
    erro = None
    contador = 0
    while contador <= 10:
        try:
            if img is None:
                img = pyautogui.locateOnScreen(
                    fr'.\public\{resolucao}\input_filter.png')
            time.sleep(0.5)
            pywinauto.mouse.double_click(button='left', coords=((img[0] + 25), (img[1] + 10)))
            time.sleep(0.5)
            pywinauto.mouse.double_click(button='left', coords=((img[0] + 25), (img[1] + 10)))
            log_info(f'coord btn ok= {img[0]}, {img[1]}')
            return img
        except Exception as e:
            log_warning(f'Houve um erro na funcão {inspect.currentframe().f_code.co_name}, aguarde...')
            contador += 1
            time.sleep(0.5)
            erro = traceback.format_exc()

    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_item_cookies(img):
    erro = None
    contador = 0
    while contador <= 10:
        try:
            pywinauto.mouse.double_click(button='left', coords=((img[0]), (img[1]+50)))
            log_info(f'coord btn ok= {img[0]}, {img[1]}')
            return
        except Exception as e:
            log_warning(f'Houve um erro na funcão {inspect.currentframe().f_code.co_name}, aguarde...')
            contador += 1
            time.sleep(0.5)
            erro = traceback.format_exc()

    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def pegar_dados_cookie_value(resolucao):
    erro = None
    contador = 0
    while contador <= 10:
        try:
            img = pyautogui.locateOnScreen(
                fr'.\public\{resolucao}\cookie_values.png')
            time.sleep(0.5)
            pywinauto.mouse.double_click(button='left', coords=((img[0]+20), (img[1]+30)))
            keyboard.send_keys('^c')
            log_info(f'coord btn ok= {img[0]}, {img[1]}')
            return
        except Exception as e:
            log_warning(f'Houve um erro na funcão {inspect.currentframe().f_code.co_name}, aguarde...')
            contador += 1
            time.sleep(0.5)
            erro = traceback.format_exc()

    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


###############Selenium################
def iniciar_webdriver_chrome(download_dir=r'C:\Users\samuelnogueira\Downloads'):
    erro = ''
    contador = 0
    while contador < 20:
        try:
            browser = DriverManagerChrome().iniciar(download_dir)
            return browser
        except Exception as e:
            log_warning('Erro ao iniciar o webdriver, tentando novamente...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()

    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def verif_atualizacao_andamento_processo(browser):
    erro = None
    contador = 0
    while contador < 3:
        try:
            browser.implicitly_wait(5)
            elemento = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[3]/td/a')
            ))
            # elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[3]/td/a')
            # elemento.click()
            return True
        except Exception as e:
            log_warning(f'Erro ao VERIFICAR "Atualização de Andamento dos Processos"...\n{e}')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    log_warning('Erro ao clicar em "Atualização de Andamento dos Processos"...', erro)
    return False

def click_atualizacao_andamento_processo(browser):
    erro = None
    contador = 0
    while contador < 3:
        try:
            browser.implicitly_wait(5)
            elemento = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[3]/td/a')
            ))
            #elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[3]/td/a')
            elemento.click()
            #browser.execute_script("arguments[0].click();", elemento)
            return True
        except Exception as e:
            log_warning(f'Erro ao clicar em "Atualização de Andamento dos Processos"...\n{e}')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    log_warning('Erro ao clicar em "Atualização de Andamento dos Processos"...', erro)
    return False

def input_num_processo(browser, n_processo):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH,
                                            '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/input')
            elemento.send_keys(n_processo)
            return
        except Exception as e:
            log_warning('Erro ao clicar em "Input número processo"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_btn_pesquisar(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/input')
            time.sleep(1)
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "Pesquisar"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def selecionar_referencia(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[2]/select')
            Select(elemento).select_by_visible_text('CI-REEMBOLSO DESP EXTRAJUD')
            return
        except Exception as e:
            log_warning('Erro selecionar referência...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def input_andamento_processual(browser, texto):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH,
                                            '//*[@id="dsAndamentoProcessoEscritorio"]')
            elemento.send_keys(texto)
            return
        except Exception as e:
            log_warning('Erro ao clicar em "Input número processo"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


def click_btn_anexos(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr[9]/td/input[2]')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "Anexos"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def reset_iframe_principal(browser):
    contador = 0
    while contador <= 2:
        try:
            browser.switch_to.default_content()
            return
        except Exception as e:
            log_warning('Erro ao resetar e ir para o iframe principal...', e)
            contador += 1
            time.sleep(1)
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}\nTraceback do último erro: {erro}')


def entrar_iframe(browser, frame):
    contador = 0
    while contador <= 2:
        try:
            iframe = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, frame))
            )
            browser.switch_to.frame(iframe)
            return
        except Exception as e:
            log_warning('Erro ao entrar no iframe principal...', e)
            contador += 1
            time.sleep(1)
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}\nTraceback do último erro: {erro}')

def input_nome_documento(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/input')
            elemento.send_keys('REEMBOLSO')
            return
        except Exception as e:
            log_warning('Erro ao clicar no input "nome documento"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


def selecionar_tipo_anexo(browser):
    erro = None
    contador = 0
    while contador < 3:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td/select')
            Select(elemento).select_by_visible_text('REEMBOLSO DESP EXTRAJUD')
            return True
        except Exception as e:
            log_warning('Erro ao clicar no btn "tipo anexo"...', e)
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
            return False
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


def anexar_documentos(browser, caminho):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td[1]/input')
            elemento.send_keys(caminho)
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "Anexar documentos"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


def click_incluir(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[7]/td/input[1]')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "Incluir"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')

def click_ok_alert_erro(browser):
    try:
        wait = WebDriverWait(browser, timeout=3)
        alert = wait.until(lambda d: d.switch_to.alert)
        text = alert.text
        log_info(text)
        alert.accept()
        return text
    except Exception as e:
        time.sleep(1)
        log_warning(e)
        return None

def click_x(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH,
                                            '//*[@id="pop"]/table/tbody/tr[1]/td/a')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "X"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


def click_salvar(browser):
    erro = None
    contador = 0
    while contador < 40:
        try:
            browser.implicitly_wait(30)
            elemento = browser.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr[9]/td/input[1]')
            elemento.click()
            return
        except Exception as e:
            log_warning('Erro ao clicar no btn "Salvar"...')
            time.sleep(0.5)
            contador += 1
            erro = traceback.format_exc()
    raise Exception(f'Erro na função: {inspect.currentframe().f_code.co_name}.\nTraceback do último erro: {erro}')


def click_ok_alert(browser):
    contador = 0
    while contador <= 5:
        try:
            wait = WebDriverWait(browser, timeout=10)
            alert = wait.until(lambda d: d.switch_to.alert)
            text = alert.text
            log_info(text)
            alert.accept()
            return text
        except Exception as e:
            time.sleep(1)
            log_warning(e)
            contador += 1
    return None