import pandas as pd
import openpyxl
import time

from src.reg_log import log_warning


def get_df(caminho):
    contador = 0
    while contador < 3:
        try:
            df = pd.read_excel(caminho, engine='openpyxl')
            return df
        except FileNotFoundError as e:
            log_warning(f'Erro ao localizar a planilha no caminho: {caminho}\n'
                  f'Tentando novamente em 10 segundos')
            time.sleep(1)
            contador += 1
        except Exception as e:
            log_warning(f'Erro ao ler a planilha, pode ser que ela esteja aberta, feche-a...\n')
            time.sleep(1)
            contador += 1
    return None

def new_df():
    return pd.DataFrame()