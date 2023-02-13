# importando a biblioteca textwrap para formatar o texto
import textwrap

# importando as bibliotecas de reconhecimento de voz e interface gráfica
import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog, Label
from tkinter import messagebox
from tkinter import Label

# importando a biblioteca moviepy para manipulação de arquivos de vídeo
from moviepy.editor import VideoFileClip
import os

# função para converter o arquivo de vídeo em um arquivo de áudio
def convert_audio(video_file):
    # carregando o arquivo de vídeo
    clip = VideoFileClip(video_file)
    # definindo o nome do arquivo de áudio a partir do nome do arquivo de vídeo
    audio_file = video_file.split(".")[0] + ".wav"
    # convertendo o áudio e salvando em um arquivo
    clip.audio.write_audiofile(audio_file)
    return audio_file

# função para reconhecer o áudio
def recognize_audio(audio_file):
    # inicializando o reconhecedor
    r = sr.Recognizer()
    # carregando o arquivo de áudio
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    try:
        # reconhecendo o áudio usando o Google Speech Recognition
        result = r.recognize_google(audio, show_all=False)
        return result
    except sr.UnknownValueError:
        # caso o áudio não possa ser compreendido
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        # caso ocorra algum erro na requisição
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

# função para selecionar o arquivo de vídeo
def select_file():
    # abrindo a caixa de diálogo para seleção de arquivo
    file_path = filedialog.askopenfilename()
    if file_path:
        # convertendo o arquivo de vídeo em áudio
        audio_file = convert_audio(file_path)
        # reconhecendo o áudio
        result = recognize_audio(audio_file)
        # formatando o texto reconhecido
        wrapped_text = textwrap.fill(result, width=40)
        # atualizando o texto na interface gráfica
        result_label.config(text=wrapped_text, font=16)
    else:
        # exibindo mensagem de erro caso o arquivo selecionado seja inválido
        messagebox.showerror("Error", "Invalid file")

# criando a janela principal da interface gráfica
root = tk.Tk()
root.title("Speech Recognition")

#criando o label para exibir o resultado do reconhecimento de fala
result_label = Label(root, text="")
result_label.pack()

#criando o botão para selecionar o arquivo de vídeo
select_file_button = tk.Button(root, text="Select file", command=select_file)
select_file_button.pack()

#iniciando a janela principal
root.mainloop()

#no final do script, a interface gráfica é iniciada e o usuário pode selecionar o arquivo de vídeo,
# que é convertido para áudio e reconhecido usando o Google Speech Recognition.
# O resultado é exibido na interface gráfica.