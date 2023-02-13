# importando a biblioteca moviepy e as biblioteca para interface grafica
from moviepy.editor import *
from tkinter import *
from tkinter import filedialog

# funcao responsavel por realizar a conversão
def convert_video():
    # abre a janela de seleção de arquivos para selecionar o video
    video_file = filedialog.askopenfilename(title = "Selecione o arquivo de vídeo", filetypes = (("mp4 files", "*.mp4"), ("all files", "*.*")))
    # abre a janela para selecionar onde salvar o arquivo de audio
    audio_file = filedialog.asksaveasfilename(title = "Salvar arquivo de audio", defaultextension=".mp3")
    # carrega o video selecionado
    video = VideoFileClip(video_file)
    # extrai o audio do video e salva em audio_file
    video.audio.write_audiofile(audio_file)

# criação da janela principal
root = Tk()
root.title("Conversor de video para mp3")
root.geometry("200x50")

# criação do botao convert
convert_button = Button(root, text="Converter", command=convert_video)
convert_button.pack()

# inicialização da janela
root.mainloop()
