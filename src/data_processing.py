from src.data_output import salvar_planilha


def preencher_e_salvar_df_passivo_ativo(df_conclusao_passivo, df_conclusao_ativo,
                                    caminho_planilha_passivo, caminho_planilha_ativo,
                                    id_solicitacao):

    indice = len(df_conclusao_passivo)
    nova_linha = {
        'IDDIL_DILIGENCIA': id_solicitacao,
        'MEMO_FOLLOWUP': 'PAGAMENTO OK',
        'USUARIO': 'samuelnogueira',
        'AUTORIZADO': 'sim',
        'STATUS_FINAL': 'REALIZADO',
        'STATUS_FINAL_MOTIVO': 'GUIA OK',
        'SOLICITAR_SOMENTE': 'não',
    }
    df_conclusao_passivo.loc[indice] = nova_linha
    salvar_planilha(df_conclusao_passivo, caminho_planilha_passivo)


    indice = len(df_conclusao_ativo)
    nova_linha = {
    'IDDIL_DILIGENCIA': id_solicitacao,
    'MEMO_FOLLOWUP': 'PAGAMENTO OK',
    'USUARIO': 'samuelnogueira',
    'AUTORIZADO': 'sim',
    'SOLICITAR_SOMENTE': 'não'
    }
    df_conclusao_ativo.loc[indice] = nova_linha
    salvar_planilha(df_conclusao_ativo, caminho_planilha_ativo)
