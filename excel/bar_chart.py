from os import system
from re import X
system("clear")

from openpyxl import Workbook 
from openpyxl.chart import BarChart 

wb = Workbook()
ws = wb.active

values = [1,2,3,4,5,6]
chart = BarChart()
chart.add_data(values)

ws.add_chart(chart, "A1")

wb.save("charts.xlsx")