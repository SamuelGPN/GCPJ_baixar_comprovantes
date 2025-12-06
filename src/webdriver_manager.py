# webdriver_manager.py
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as OptionsMozilla
from selenium.webdriver.chrome.options import Options as OptionsChrome
from src.reg_log import log_error


class DriverManagerChrome:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.driver = None
        return cls._instancia

    def iniciar(self, download_dir):
        if self.driver is None:
            options = OptionsChrome()
            chromedriver_path = rf'.\webdrivers\chromedriver.exe'
            service = Service(chromedriver_path)
            prefs = {
                "download.default_directory": download_dir,  # pasta de destino
                "download.prompt_for_download": False,  # não perguntar onde salvar
                "download.directory_upgrade": True,  # atualizar pasta se mudar
                "safebrowsing.enabled": True  # evitar bloqueios de segurança
            }
            options.add_experimental_option("prefs", prefs)
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options, service=service)
        return self.driver

    def get_driver(self):
        return self.driver

class DriverManagerMozilla:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.driver = None
        return cls._instancia

    def iniciar(self, profile_path):
        if self.driver is None:
            # Cria o perfil
            profile = FirefoxProfile(profile_path)

            # Define opções (ex: evitar detecção de automação)
            options = OptionsMozilla()

            options.profile = profile
            options.add_argument("--disable-blink-features=AutomationControlled")

            # Inicia o navegador com o perfil
            self.driver = webdriver.Firefox(options=options)
        return self.driver

    def get_driver(self):
        return self.driver

    def encerrar(self):
        if self.driver:
            self.driver.quit()