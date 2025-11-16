import os
import shutil
from os.path import isfile, join
from pypdf import PdfReader
from pypdf.errors import EmptyFileError

def remover_arquivos_olds(caminho):
    # Percorre todos os itens da pasta
    for item in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, item)

        # Verifica se é um arquivo (e não uma pasta)
        if os.path.isfile(caminho_completo):
            try:
                os.remove(caminho_completo)
                print(f'Arquivo removido: {caminho_completo}')
            except Exception as e:
                print(f'Erro ao remover {caminho_completo}: {e}')


def procurar_cod_barras_em_pdf(caminho_comprovantes_downloads, caminho_comprovantes_ok,  codigo, n_gcpj, id_custa, valor):
    arquivos = [f for f in os.listdir(caminho_comprovantes_downloads) if isfile(join(caminho_comprovantes_downloads, f))]
    print(arquivos)

    for a in arquivos:
        path_completo_pdf = fr'{caminho_comprovantes_downloads}\{a}'
        try:
            if a.lower().endswith('.pdf'):
                reader = PdfReader(path_completo_pdf)
        except EmptyFileError as e:
            os.remove(path_completo_pdf)
            print(f'Arquivo {a} vazio ou corrompido.')
        except Exception as e:
            print('Erro desconhecido.', e)


    arquivos = [f for f in os.listdir(caminho_comprovantes_downloads) if isfile(join(caminho_comprovantes_downloads, f))]
    print(arquivos)

    lista_cod_ok = []
    for a in arquivos:
        caminho_arq = rf'{caminho_comprovantes_downloads}\{a}'
        if a.lower().endswith('.pdf'):
            reader = PdfReader(caminho_arq)

            if len(reader.pages) > 0:
                page = reader.pages[0]
                # continue com o processamento
            else:
                print("O PDF não contém páginas.")
                continue

            text = page.extract_text()
            text_formatado = text.replace(' ', '').replace('.', '').replace('-', '').replace('/', '').strip()
            try:
                if codigo in text_formatado and str(format(valor, '.2f')) in text_formatado.replace(',', '.') and '60746948000112' in text_formatado:
                    print(f'Sucesso!\n cod: {codigo} em {a}\n')
                    shutil.copy(caminho_arq, f'{caminho_comprovantes_ok}/{id_custa}.pdf')
                    #lista_cod_ok.append(codigo)
                    #lista_cod_barras.remove(c)
                    return True
            except EmptyFileError as e:
                print(f'Arquivo {a} vazio ou corrompido.')
            except Exception as e:
                print('Erro desconhecido.', e)
    return False