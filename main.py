import PyPDF2

pdf_in = open('sample.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

clockWise = [1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 21, 22, 36, 37, 38, 39, 40, 44, 45, 46, 47, 48, 49] # page numbers in index 0 format which have to be oriented clockwise
antiClockWise = [5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 29, 32, 33, 41, 42, 43] # page numbers in index 0 format which have to be oriented Anti-clockwise

# Only 50 pages inside the pdf file
for pagenum in range(50):
    print("Current Page is: %d" %(pagenum+1))
    page = pdf_reader.getPage(pagenum)
    if pagenum in clockWise:
        print("Page #%d is rotated Clockwise!" %(pagenum+1))
        page.rotateClockwise(90) # rotating clockwise
    elif pagenum in antiClockWise:
        print("Page #%d is rotated Anti-Clockwise!" %(pagenum+1))
        page.rotateClockwise(-90) # rotating Anti-clockwise
    else:
        print("Page #%d is Perfect!" %(pagenum+1))
    print("\n")
    pdf_writer.addPage(page)


pdf_out = open('sample-aligned.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
