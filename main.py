import os
from src.config import CAMINHO_DIR_JAR, CAMINHO_ARQ_JAR, URL_GCPJ, CAMINHO_PASTA_DOCUMENTOS_GCPJ, CAMINHO_CERT, \
    CAMINHO_PASTA_PLANILHA_BASE_GCPJ, CAMINHO_CONCLUIDOS, CAMINHO_PASTA_LOTES_MULTIPAG, CAMINHO_PASTA_BAIXADOS_DIVERSOS
from src.file_handling import create_folder
from src.main_processing import executar_arquivo, pegar_cookies_gcpj, lancar_anexos, baixar_comprovantes
from src.reg_log import log_info, log_error
from src.utils import pegar_data_hora


def main(caminho_concluidos, lotes, dt_cookie=None, jsession_id=None, resolucao=None):
    if int(pegar_data_hora()[7]) < 2026:
        create_folder(r'.\envs\GCPJ_inclusao')
        create_folder(r'.\logs\GCPJ_Inclusao')
        create_folder(CAMINHO_PASTA_BAIXADOS_DIVERSOS)

        if resolucao:
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

        else:
            cookies = [
                {'name': 'dtCookie', 'value': f'{dt_cookie}'},
                {'name': 'JSESSIONID', 'value': f'{jsession_id}'}
            ]
            if not dt_cookie or not jsession_id:
                raise Exception('Os dados dos cookies não foram colocados corretamente!')
            elif not lotes:
                raise Exception('Os dados do lote não foram colocados corretamente!')
            elif not caminho_concluidos:
                raise Exception('O caminho da pasta dos lotes concluídos não foi colocado corretamente!')
            #lancar_anexos(cookies, URL_GCPJ, CAMINHO_PASTA_PLANILHA_BASE_GCPJ, CAMINHO_PASTA_DOCUMENTOS_GCPJ)

        for _ in range(2):
            baixar_comprovantes(lotes, cookies, URL_GCPJ, CAMINHO_PASTA_LOTES_MULTIPAG,
                                caminho_concluidos, CAMINHO_PASTA_BAIXADOS_DIVERSOS)
    else:
        raise Exception('Versão expirada, contate o ADM.')
if __name__ == '__main__':
    main(CAMINHO_CONCLUIDOS, lotes=[13736, 13737, 13738, 13739], resolucao='1920X1080')
