import threading
from tkinter import Tk, StringVar, ttk, N, W, E, S
from tkinter.ttk import Button

from main import main


def iniciar_em_thread():
    threading.Thread(target=iniciar).start()

def iniciar():
    info_label.config(text="🔄 Executando...")
    try:
        main(lotes=input_Lotes.get(), dt_cookie=input_Dt_Cookies.get(), jsession_id=input_Jsession_Id.get())
        info_label.config(text="✅ Concluído!")
    except Exception as e:
        info_label.config(text=f'{e}')

root = Tk()
root.title('Baixar_comprovante_BS')
mensagem = StringVar()

janela = ttk.Frame(root, padding="3 3 12 12")
janela.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(janela, text='Selecione o(s) lote(s), Exemplo: 15957, 14968,...').grid(column=1, row=1, sticky=(W))
Lotes = StringVar()
input_Lotes = ttk.Entry(janela, width=45, textvariable=Lotes)
input_Lotes.grid(column=1, row=2, sticky=(E))

ttk.Label(janela, text="dt_cookies: ").grid(column=1, row=3, sticky=(W))
dt_cookies = StringVar()

input_Dt_Cookies = ttk.Entry(janela, width=45, textvariable=dt_cookies)
input_Dt_Cookies.grid(column=1, row=4, sticky=(E))

ttk.Label(janela, text="jsession_id: ").grid(column=1, row=5, sticky=(W))
jsession_id = StringVar()

input_Jsession_Id = ttk.Entry(janela, width=45, textvariable=jsession_id)
input_Jsession_Id.grid(column=1, row=6, sticky=(E))

BtnOK = Button(janela, text='OK', command=iniciar_em_thread).grid(column=1, row=7, sticky=W)


label_erro = ttk.Label(janela, textvariable=mensagem, foreground='red')
label_erro.grid(column=1, row=8, columnspan=2, sticky=(W), pady=5)

info_label = ttk.Label(janela, text="...")
info_label.grid(column=1, row=9, columnspan=2, pady=5)

root.mainloop()