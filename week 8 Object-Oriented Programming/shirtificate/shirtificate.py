from fpdf import FPDF

width = 210
height = 297

shirt_width = 150
shirt_height = 150

x = (width-shirt_width)/2
y = (height-shirt_height)/2

name = input("Enter your name: ")

pdf = FPDF(orientation = 'p',unit='mm',format="A4")
pdf.add_page()
pdf.set_font("Arial",style="B",size=24)

title = "CS50 Shirtificate"
title_w = pdf.get_string_width(title)
title_x = (width-title_w)/2
pdf.text(title_x,15,title)

pdf.image('shirtificate.png',x=x,y=y,w=shirt_width)

pdf.set_text_color(255,255,255)

name_w = pdf.get_string_width(name)
name_x = (width-name_w)/2
name_y = (y + shirt_height)/2 - 12
pdf.text(name_x,name_y,name)

pdf.output('shirtificate.pdf')