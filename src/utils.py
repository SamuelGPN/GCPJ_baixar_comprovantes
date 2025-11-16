import time
import clipboard

def pegar_data_hora():
    data = time.strftime("%d/%m/%Y", time.localtime())
    dataehora = time.strftime("%d_%m_%Y__%H", time.localtime())
    data_formatada = time.strftime("%d_%m_%Y", time.localtime())
    data_formatada2 = time.strftime("%Y%m%d", time.localtime())
    hora_min_seg = time.strftime("%H%M%S", time.localtime())
    hora = time.strftime("%H", time.localtime())
    dataehora2 = time.strftime("%d_%m_%Y__%H%M%S", time.localtime())

    dataehora_list = [data, dataehora, data_formatada, data_formatada2, hora_min_seg, hora, dataehora2]
    return dataehora_list

def pegar_text_area_tranferencia():
    # Colar texto da área de transferência
    texto = clipboard.paste()
    return texto