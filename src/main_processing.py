import os
import platform
import subprocess
import time
import psutil
from tabnanny import check

import pandas as pd

from selenium.webdriver.common.by import By

from src.GUI_automation import verificar_menu, press_f12, click_setas_dev_tools, click_btn_application, \
    click_btn_cookies, click_input_filter, escrever, pegar_dados_cookie_value, click_item_cookies, \
    iniciar_webdriver_chrome, input_num_processo, click_atualizacao_andamento_processo, click_btn_pesquisar, \
    selecionar_referencia, input_andamento_processual, click_btn_anexos, entrar_iframe, input_nome_documento, \
    anexar_documentos, selecionar_tipo_anexo, click_incluir, click_ok_alert_erro, click_salvar, click_ok_alert, \
    verif_atualizacao_andamento_processo, click_x, reset_iframe_principal
from src.baixar_comprovantes.GUI_automation import verif_incluir_anexo, click_incluir_anexo, \
    input_num_processo_comprovante, click_btn_duas_setas_direita, click_btn_pesquisar_comprovante, find_table, \
    click_visualizar_arq, click_btn_voltar, click_x_comprovante, click_btn_uma_seta_esquerda
from src.baixar_comprovantes.file_handling import remover_arquivos_olds, procurar_cod_barras_em_pdf
from src.config import URL_GCPJ, CAMINHO_PASTA_BAIXADOS_DIVERSOS
from src.data_input import get_df
from src.data_output import salvar_planilha
from src.data_processing import preencher_e_salvar_df_passivo_ativo
from src.file_handling import create_folder
from src.reg_log import log_info, log_error
from src.utils import pegar_text_area_tranferencia, pegar_data_hora


def executar_arquivo(caminho, diretorio):
    from src.reg_log import log_info

    log_info('Executando o .jar, aguarde...')
    if platform.system() == 'Windows':
        # os.startfile(caminho)

        comando = ['java', '-jar', caminho]
        res = subprocess.Popen(
            comando,
            cwd=diretorio,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Interpreta entrada/saída como texto (string)
        )
        log_info('O .jar foi eecutado com sucesso!')
        return res
    return None


def pegar_cookies_gcpj(processo, resolucao):
    verificar_menu(resolucao)
    press_f12()
    click_setas_dev_tools(resolucao)
    click_btn_application(resolucao)
    click_btn_cookies(resolucao)
    img_filter = click_input_filter(resolucao)
    escrever('dtCookie')
    click_item_cookies(img_filter)
    pegar_dados_cookie_value(resolucao)
    value_dt_cookie = pegar_text_area_tranferencia()
    click_input_filter(resolucao, img_filter)
    escrever('JSESSIONID')
    click_item_cookies(img_filter)
    pegar_dados_cookie_value(resolucao)
    value_jsessionid = pegar_text_area_tranferencia()
    log_info(f'{value_dt_cookie}, {value_jsessionid}')
    cookies = [
        {'name': 'dtCookie', 'value': f'{value_jsessionid}'},
        {'name': 'JSESSIONID', 'value': f'{value_jsessionid}'}
    ]

    parent = psutil.Process(processo.pid)
    for child in parent.children(recursive=True):
        child.kill()
    try:
        parent.kill()
    except:
        pass
    return cookies

def preparar_arquivos():

    pass


def lancar_anexos(cookies, site, caminho_pasta_planilha_base_gcpj, caminho_pasta_documentos_gcpj):
    caminho_planilha_base_gcpj = fr"{caminho_pasta_planilha_base_gcpj}\gcpj_inclusao_{pegar_data_hora()[2]}.xlsx"
    caminho_pdfs = fr"{caminho_pasta_documentos_gcpj}\{pegar_data_hora()[2]}\PDFs"
    create_folder(caminho_pdfs)

    lista_pdfs = os.listdir(caminho_pdfs)

    df = get_df(caminho_planilha_base_gcpj)
    df_copia = df.copy()

    browser = iniciar_webdriver_chrome()
    browser.get(site)

    browser.delete_all_cookies()

    for cookie in cookies:
        browser.add_cookie(cookie)

    browser.refresh()

    entrar_iframe(browser, '/html/frameset/frame[3]')
    if not verif_atualizacao_andamento_processo(browser):
        browser.delete_all_cookies()
        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()
        time.sleep(5)
        if not verif_atualizacao_andamento_processo(browser):
            msg = 'Não foi possível achar o elemento "atualização andamento do processo"'
            log_error(msg)
            raise Exception(msg)

    click_atualizacao_andamento_processo(browser)
    for index, linha in df.iterrows():
        n_gcpj = linha['Número de Controle do Cliente']
        id_custa = linha['ID Custa']
        log_info(id_custa)

        if f"{id_custa}.pdf" not in lista_pdfs:
            df_copia.at[index, 'STATUS'] = 'NÃO ENCONTRADA AS INCLUSÕES, VERIFIQUE'
            salvar_planilha(df_copia, caminho_planilha_base_gcpj)
            continue


        input_num_processo(browser, str(n_gcpj))
        click_btn_pesquisar(browser)
        selecionar_referencia(browser)
        input_andamento_processual(browser, 'REEMBOLSO')
        click_btn_anexos(browser)
        entrar_iframe(browser, '//*[@id="here"]')
        input_nome_documento(browser)
        if not selecionar_tipo_anexo(browser):
            reset_iframe_principal(browser)
            entrar_iframe(browser, '/html/frameset/frame[3]')
            click_x(browser)
            click_btn_anexos(browser)
            entrar_iframe(browser, '//*[@id="here"]')
            input_nome_documento(browser)
            if not selecionar_tipo_anexo(browser):
                msg = 'Não foi possível selecionar o tipo do anexo, verifique o log de erros...'
                log_error(msg)
                raise Exception(msg)
        anexar_documentos(browser, fr'{caminho_pdfs}\{id_custa}.pdf')
        click_incluir(browser)
        #click_ok_alert_erro(browser)
        time.sleep(3)
        reset_iframe_principal(browser)
        entrar_iframe(browser, '/html/frameset/frame[3]')
        click_x(browser)
        click_salvar(browser)
        click_ok_alert(browser)
        #browser.get(site)
        log_info('Sucesso!')
        reset_iframe_principal(browser)
        entrar_iframe(browser, '/html/frameset/frame[3]')
        time.sleep(3)

def baixar_comprovantes(cookies, site,
                        caminho_pasta_lotes_multipag,
                        caminho_concluidos,
                        caminho_pasta_baixados_diversos):

    lotes = [13711]
    inicio = time.time()  # Marca o tempo inicial;

    browser = iniciar_webdriver_chrome(caminho_pasta_baixados_diversos)
    browser.get(site)

    browser.delete_all_cookies()

    for cookie in cookies:
        browser.add_cookie(cookie)

    browser.refresh()

    entrar_iframe(browser, '/html/frameset/frame[3]')
    if not verif_incluir_anexo(browser):
        browser.delete_all_cookies()
        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()
        time.sleep(5)
        if not verif_incluir_anexo(browser):
            msg = 'Não foi possível achar o elemento "atualização andamento do processo"'
            log_error(msg)
            raise Exception(msg)

    for lote in lotes:
        nome_pasta_lote = ''
        lista_pastas_lotes = os.listdir(caminho_pasta_lotes_multipag)
        for pasta in lista_pastas_lotes:
            if f'{lote} ' in pasta:
                nome_pasta_lote = pasta
                break

        caminho_planilha_lote = ''
        lista_arquivos_pasta_lote = os.listdir(rf'{caminho_pasta_lotes_multipag}\{nome_pasta_lote}')
        for arq in lista_arquivos_pasta_lote:
            if 'ID CUSTA.' in arq:
                caminho_planilha_lote = rf'{caminho_pasta_lotes_multipag}\{nome_pasta_lote}\{arq}'
                break

        df = get_df(caminho_planilha_lote)

        log_info(f'Lote: {lote}')

        create_folder(caminho_pasta_baixados_diversos)
        remover_arquivos_olds(caminho_pasta_baixados_diversos)

        caminho_comprovantes_ok = rf'{caminho_concluidos}\LOTE {lote}\comprovantes'
        caminho_planilha_status = rf'{caminho_concluidos}\LOTE {lote}\status_planilha_{lote}.xlsx'
        caminho_planilha_passivo = rf'{caminho_concluidos}\LOTE {lote}\PASSIVO.xlsx'
        caminho_planilha_ativo = rf'{caminho_concluidos}\LOTE {lote}\ATIVO.xlsx'

        create_folder(caminho_comprovantes_ok)

        df_conclusao_passivo = get_df(caminho_planilha_passivo)
        if df_conclusao_passivo is None:
            df_conclusao_passivo = pd.DataFrame(
                columns=['IDDIL_DILIGENCIA', 'MEMO_FOLLOWUP', 'USUARIO',
                         'AUTORIZADO', 'STATUS_FINAL',
                         'STATUS_FINAL_MOTIVO', 'OBSERVACAO',
                         'SOLICITAR_SOMENTE'])

        df_conclusao_ativo = get_df(caminho_planilha_ativo)
        if df_conclusao_ativo is None:
            df_conclusao_ativo = pd.DataFrame(
                columns=['IDDIL_DILIGENCIA', 'MEMO_FOLLOWUP', 'USUARIO',
                         'AUTORIZADO', 'STATUS_FINAL',
                         'STATUS_FINAL_MOTIVO',
                         'OBSERVACAO', 'SOLICITAR_SOMENTE'])

        status_df = get_df(caminho_planilha_status)
        if status_df is None:
            status_df = pd.DataFrame(
                columns=['Nº               GCPJ', 'ID CUSTA',
                         'VALOR', 'CODIGO BARRAS', 'ID SOLICITAÇÃO',
                         'STATUS'])

        for index, linha in df.iterrows():
            try:
                n_gcpj = linha['Nº               GCPJ']
                id_custa = linha['ID CUSTA']
                id_solicitacao = linha['ID SOLICITAÇÃO']
                valor = linha['VALOR']
                cod_barras = linha['CODIGO BARRAS']

                if not pd.isna(n_gcpj) and not pd.isna(valor) and not pd.isna(cod_barras) and not pd.isna(
                        id_custa) and not pd.isna(id_solicitacao):
                    status_df.at[index, 'Nº               GCPJ'] = n_gcpj
                    status_df.at[index, 'ID CUSTA'] = id_custa
                    status_df.at[index, 'ID SOLICITAÇÃO'] = id_solicitacao
                    status_df.at[index, 'VALOR'] = valor
                    status_df.at[index, 'CODIGO BARRAS'] = cod_barras

                else:
                    raise Exception(f'Há linhas vazias.')

            except ValueError:
                print(f'Erro ao converter a linha {index} para int.')

            except Exception as e:
                print(f'Erro desconhecido na linha {index}.', e)


        click_incluir_anexo(browser)
        for index, linha in status_df.iterrows():
            n_gcpj = int(float(str(linha['Nº               GCPJ']).strip()))
            id_custa = int(float(str(linha['ID CUSTA']).strip()))
            id_solicitacao = linha['ID SOLICITAÇÃO']
            valor = linha['VALOR']
            cod_barras = linha['CODIGO BARRAS']
            status = linha['STATUS']

            if 'OK' in str(status):
                continue

            if len(str(n_gcpj)) < 10:
                n_gcpj = str(n_gcpj).zfill(10)

            log_info(f'numero de processo: {n_gcpj}')
            log_info(f'index: {index}')

            input_num_processo_comprovante(browser, n_gcpj)
            click_btn_pesquisar_comprovante(browser)
            try:
                click_btn_duas_setas_direita(browser)
            except:
                browser.refresh()
                entrar_iframe(browser, '/html/frameset/frame[3]')
                click_incluir_anexo(browser)
                status_df.at[index, 'STATUS'] = 'False'
                salvar_planilha(status_df, caminho_planilha_status)
                continue
            time.sleep(1)

            contador = 0
            while contador < 20: #Verifica se a linha contém data, senão ele pula para a tabela à esquerda.
                linhas = find_table(browser)
                celula_data_text = linhas[2].find_element(By.XPATH, './td[7]').text
                if celula_data_text == '':
                    click_btn_uma_seta_esquerda(browser)
                    time.sleep(2)
                else:
                    break
                contador += 1

            #Deleta o último item da lista
            linhas.pop()

            for i, tr in enumerate(linhas):
                if i < 2:
                    continue
                celula_checkbox = tr.find_element(By.XPATH, './td[1]/input')
                celula_checkbox.click()
                click_visualizar_arq(browser)
                click_x_comprovante(browser)
                celula_checkbox.click()
            click_btn_voltar(browser)
            time.sleep(2)
            encontrar_pdf_com_cod_barras = procurar_cod_barras_em_pdf(caminho_pasta_baixados_diversos,
                                                                      caminho_comprovantes_ok, cod_barras, n_gcpj,
                                                                      id_custa, valor)
            log_info(f'encontrar_pdf_com_cod_barras: {encontrar_pdf_com_cod_barras}')
            if encontrar_pdf_com_cod_barras:
                status_df.at[index, 'STATUS'] = 'OK'
                salvar_planilha(status_df, caminho_planilha_status)

                preencher_e_salvar_df_passivo_ativo(df_conclusao_passivo,
                                                    df_conclusao_ativo,
                                                    caminho_planilha_passivo,
                                                    caminho_planilha_ativo,
                                                    id_solicitacao)

            else:
                status_df.at[index, 'STATUS'] = 'False'
                salvar_planilha(status_df, caminho_planilha_status)




    fim = time.time()  # Marca o tempo final
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")