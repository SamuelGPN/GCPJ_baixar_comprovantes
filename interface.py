import threading
from tkinter import Tk, StringVar, ttk, filedialog
from tkinter.ttk import Button
from tkinter import*



def escolher_pasta():
    global Pasta_selecionada
    mensagem.set('')

    info_label.config(text="...")
    try:
        Pasta_selecionada = filedialog.askdirectory(
            title='Selecione uma Pasta: ')
        print(Pasta_selecionada)
        caminhoPaste.set(f'{Pasta_selecionada}')
        get_pasta = input_Paste.get()
        print('Caminho da Pasta: ', get_pasta)
    except Exception as error:
        print('ERRO AO ESCOLHER A PASTA: ', error)

def iniciar_em_thread():
    threading.Thread(target=iniciar).start()

def iniciar():
    from main import main
    info_label.config(text="🔄 Executando...")
    try:
        lotes = input_Lotes.get().replace(' ', '').split(',')

        main(caminho_concluidos=input_Paste.get(), lotes=lotes, dt_cookie=input_Dt_Cookies.get(), jsession_id=input_Jsession_Id.get())
        info_label.config(text="✅ Concluído!")
    except Exception as e:
        info_label.config(text=f'{e}')

root = Tk()
root.title('Baixar_comprovante_BS')
mensagem = StringVar()

frame1 = ttk.Frame(root, padding="3 3 12 12")
frame1.grid(column=0, row=1, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame2 = ttk.Frame(root, padding="3 3 12 12")
frame2.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(frame1, text='Selecione o(s) lote(s), Exemplo: 15957, 14968,...').grid(column=1, row=1, sticky=(W))
Lotes = StringVar()
input_Lotes = ttk.Entry(frame1, width=45, textvariable=Lotes)
input_Lotes.grid(column=1, row=2, sticky=(E))

ttk.Label(frame1, text="dt_cookies: ").grid(column=1, row=3, sticky=(W))
dt_cookies = StringVar()

input_Dt_Cookies = ttk.Entry(frame1, width=45, textvariable=dt_cookies)
input_Dt_Cookies.grid(column=1, row=4, sticky=(E))

ttk.Label(frame1, text="jsession_id: ").grid(column=1, row=5, sticky=(W))
jsession_id = StringVar()

input_Jsession_Id = ttk.Entry(frame1, width=45, textvariable=jsession_id)
input_Jsession_Id.grid(column=1, row=6, sticky=(E))

ttk.Label(frame2, text="Caminho da pasta dos lotes concluídos: ").grid(column=2, row=1, sticky=(W))
caminhoPaste = StringVar()
#caminhoPaste.set(caminho_padrao)
input_Paste = ttk.Entry(frame2, width=45, textvariable=caminhoPaste)
input_Paste.grid(column=2, row=2, sticky=(E))
BtnAdd_Paste = Button(frame2, text='+', command=escolher_pasta).grid(column=1, row=2, sticky=(W))

BtnOK = Button(frame1, text='OK', command=iniciar_em_thread).grid(column=1, row=7, sticky=W)


label_erro = ttk.Label(frame1, textvariable=mensagem, foreground='red')
label_erro.grid(column=1, row=8, columnspan=2, sticky=(W), pady=5)

info_label = ttk.Label(frame1, text="...")
info_label.grid(column=1, row=9, columnspan=2, pady=5)

root.mainloop()