import os
from src.config import CAMINHO_DIR_JAR, CAMINHO_ARQ_JAR, URL_GCPJ, CAMINHO_PASTA_DOCUMENTOS_GCPJ, CAMINHO_CERT, \
    CAMINHO_PASTA_PLANILHA_BASE_GCPJ, CAMINHO_CONCLUIDOS, CAMINHO_PASTA_LOTES_MULTIPAG, CAMINHO_PASTA_BAIXADOS_DIVERSOS
from src.file_handling import create_folder
from src.main_processing import executar_arquivo, pegar_cookies_gcpj, lancar_anexos, baixar_comprovantes
from src.reg_log import log_info, log_error
from src.utils import pegar_data_hora


def main(resolucao):
    create_folder(r'.\envs\GCPJ_inclusao')
    create_folder(r'.\logs\GCPJ_Inclusao')


    if os.path.exists(CAMINHO_CERT):
        log_info('O certificado de Danilo Silva foi encontrado!!')
        if os.path.exists(CAMINHO_ARQ_JAR):
            log_info('O arquivo .jar foi encontrado!!')
        else:
            msg = 'O arquivo .jar não foi encontrado, encerrando o robô...'
            log_error(msg)
            raise Exception(msg)
    else:
        msg = 'O certificado de DANILO SILVA não foi encontrado, encerrando o robô...'
        log_error(msg)
        raise Exception(msg)
        
    processo = executar_arquivo(CAMINHO_ARQ_JAR, CAMINHO_DIR_JAR)
    if processo is None:
        raise Exception('O processo do arquivo (.jar) não foi executado... Encerrando o robô.')
    cookies = pegar_cookies_gcpj(processo, resolucao)
    if cookies is None:
        raise Exception('Não foi encontrado os valores dos cookies... Encerrando o robô.')

    #cookies = [
    #    {'name': 'dtCookie', 'value': f'v_4_srv_70_sn_55A39EB74BCB0D8B8FCE71F38A8356E6_perc_100000_ol_0_mul_1_app-3A004bcf58b40a0c0d_1'},
    #    {'name': 'JSESSIONID', 'value': f'0000UPPclMr5IYCmGdfyWharcRQ:1e0r07am8'}
    #]
    #lancar_anexos(cookies, URL_GCPJ, CAMINHO_PASTA_PLANILHA_BASE_GCPJ, CAMINHO_PASTA_DOCUMENTOS_GCPJ)
    for _ in range(2):
        baixar_comprovantes(cookies, URL_GCPJ, CAMINHO_PASTA_LOTES_MULTIPAG, CAMINHO_CONCLUIDOS, CAMINHO_PASTA_BAIXADOS_DIVERSOS)
if __name__ == '__main__':
    main('1600X900')
