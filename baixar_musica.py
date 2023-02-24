
from tkinter import *
from pytube import YouTube
import os


root =  Tk()
root.title("Baixar mp3")
root.geometry("300x90")
#---------------------------------------------------------------------
# funcoes
def baixar():
    path = os.getcwd()
    link = link_input.get()
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()

    titulo = yt.title

    downloaded_file = video.download(path)
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    label1 = Label(root, text="Download concluido!")
    label2 = Label(root, text=titulo)
    label1.grid(row= 2,  column=1)
    label2.grid(row= 3,  columnspan = 3)
    link_input.delete(0,END)

#---------------------------------------------------------------------
# Layout

label_title = Label(root, text="Baixar musicas do YouTube")

label_digita = Label(root, text="Digite o link")
link_input = Entry(root)
btn = Button(root, text="Baixar", command=baixar)

label_title.grid(row= 0,  column=1)
label_digita.grid(row= 1,  column=0)
link_input.grid(row= 1,  column=1)
btn.grid(row= 1,  column=2)
#---------------------------------------------------------------------
root.mainloop()
