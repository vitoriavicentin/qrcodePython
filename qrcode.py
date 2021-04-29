#importar QRCode 
import pyqrcode
from pyqrcode import QRCode
import sys
#String que será representada pelo QRCode
s = input("Digite a url a ser transformada: ")
#Nome para o arquivo de saida 
n = input("Digite o nome de saida: ")

#Gerar o QRCode
url = pyqrcode.create(s)
#Criar e salvar o arquivo com o nome inserido
url.svg(n +".svg",scale=4)
url.png(n +".png",scale=4)