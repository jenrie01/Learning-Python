import PyPDF2

# mycode
with open('super.pdf', 'rb') as super_file:
    super_reader = PyPDF2.PdfFileReader(super_file)
    with open('wtr.pdf', 'rb') as water_file:
        water_reader = PyPDF2.PdfFileReader(water_file)
        water_page = water_reader.getPage(0)
        writer = PyPDF2.PdfFileWriter()
        for page in range(len(super_reader.pages)):
            super_page = super_reader.getPage(page)
            super_page.mergePage(water_page)
            writer.addPage(super_page)

        with open('superwtr.pdf', 'wb') as new_file:
            writer.write(new_file)

# andreicode
# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#   page = template.getPage(i)
#   page.mergePage(watermark.getPage(0))
#   output.addPage(page)

#   with open('watermarked_output.pdf', 'wb') as file:
#     output.write(file)
