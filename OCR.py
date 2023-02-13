from PIL import Image
import pytesseract

# Carregue a imagem
img = Image.open("C:/Users/vinis/Desktop/Teste/teste.jpg")

# Use o pytesseract para extrair o texto da imagem
text = pytesseract.image_to_string(img)

# Imprima o texto extraído
print(text)