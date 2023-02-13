import os
import PyPDF4

#Função para compactar o pdf
def compress_pdf(file_path):
    #Abrindo o arquivo em modo binário
    with open(file_path, "rb") as file:
        #Criando um objeto PdfFileReader com o arquivo
        pdf_reader = PyPDF4.PdfFileReader(file)
        #Criando um objeto PdfFileWriter para escrever o pdf comprimido
        pdf_writer = PyPDF4.PdfFileWriter()

        #Percorrendo as páginas do pdf original
        for page in range(pdf_reader.numPages):
            #Adicionando cada página ao pdf comprimido
            pdf_writer.addPage(pdf_reader.getPage(page))

        #Definindo o nome do pdf comprimido como o nome original do pdf mais "_compressed"
        compressed_pdf = file_path.replace(".pdf", "_compressed.pdf")
        #Abrindo o pdf comprimido em modo binário para escrita
        with open(compressed_pdf, "wb") as output:
            #Escrevendo o pdf comprimido
            pdf_writer.write(output)

#Definindo o caminho da pasta "Teste" na área de trabalho
path = os.path.join(os.path.expanduser("~"), "Desktop", "AEE")
#Percorrendo todos os arquivos na pasta "Teste"
for filename in os.listdir(path):
    #Se o arquivo for um pdf
    if filename.endswith(".pdf"):
        #Chamando a função para compactar o pdf
        compress_pdf(os.path.join(path, filename))
