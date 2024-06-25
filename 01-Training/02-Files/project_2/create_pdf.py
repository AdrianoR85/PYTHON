from fpdf import FPDF
from num2words import num2words as n2w
from datetime import date

# 1 - Variables
cliente = input("Informe o nome do Cliente: ").title()
consulta = input("Informe o tipo da consulta: ")
vlr = input("Informe o valor da consulta: ")
vlr_msg = f'{vlr} reais'
vlr_extenso = n2w(float(vlr), lang='pt-br')
vlr_extenso_msg = f'{vlr_extenso} reais'
dia = date.today().day
mes = date.today().month
ano = date.today().year

# 2 - Layout
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 20)
pdf.image("rec.jpg", x=0, y=0, w=pdf.w, h=pdf.h)
pdf.text(160, 45, vlr_msg)
pdf.text(72, 88, cliente)
pdf.text(72, 114, vlr_extenso_msg)
pdf.text(72, 140, consulta)
pdf.set_text_color(255,255,255)
pdf.text(30, 198, str(dia))
pdf.text(50, 198, str(mes))
pdf.text(70, 198, str(ano))

nome_arquivo = f'{cliente.strip()}_{dia}_{mes}_{ano}'

pdf.output(f"{nome_arquivo}.pdf")
print('Recipe created successfully!')
