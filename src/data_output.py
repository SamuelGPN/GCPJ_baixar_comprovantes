import traceback


def salvar_planilha(df, caminho):
    from src.reg_log import log_warning
    import time

    erro = None
    for _ in range(100):
        try:
            caminho_absoluto = caminho
            df.to_excel(caminho_absoluto, index=False)
            return caminho_absoluto
        except Exception as e:
            log_warning(f'Erro, a planilha {caminho}'
                  f' pode estar aberta, senão, a comunicação com o servidor pode ter sido interrompida', e)
            time.sleep(2)
            erro = traceback.format_exc()
    raise Exception(erro)