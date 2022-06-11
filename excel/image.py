from os import system
from re import X
system("clear")

from openpyxl import Workbook 
from openpyxl.drawing.image import Image 

wb = Workbook()
ws = wb.active 

img = Image('cat.jpg')
ws.add_image(img, 'E7')

img2 = Image('shark.jpg')
img2.anchor = 'A21'
ws.add_image(img2)

wb.save('cat.xlsx')

#se debe instalar pillow para que funcione
