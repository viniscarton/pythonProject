import os # importa a biblioteca os
from docx2pdf import convert # importa a biblioteca docx2pdf

def docx_to_pdf(path): # cria uma função docx_to_pdf com o parametro path
    for root, dirs, files in os.walk(path): # usa a função os.walk para percorrer recursivamente todos os arquivos e diretórios dentro do caminho especificado. A variavel root, dirs e files armazenam informações sobre o diretório atual, os subdiretórios e os arquivos, respectivamente.
        for file in files: # percorre todos os arquivos dentro do diretório
            if file.endswith(".docx"): # verifica se o arquivo é uma extensão de docx
                docx_filename = os.path.join(root, file) # cria uma variavel docx_filename com o caminho completo do arquivo
                pdf_filename = os.path.splitext(docx_filename)[0] + '.pdf' # cria uma variavel pdf_filename com o nome do arquivo original e a extensão pdf
                convert(docx_filename, pdf_filename) # usa a função convert para converter o arquivo docx para pdf
                print(f'{docx_filename} foi convertido para {pdf_filename}') # imprime o nome do arquivo original e o nome do arquivo convertido

# exemplo de uso
docx_to_pdf('C:/Users/vinis/Desktop') # chama a função docx_to_pdf e passa como parametro o caminho para o diretório
