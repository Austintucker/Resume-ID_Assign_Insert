# Resume ID Assignment and Insert

import os, PyPDF2
from fpdf import FPDF

resumeDirectory = f"{os.getcwd()}\\Resumes"
os.chdir(resumeDirectory)

i = 20 # starting Value for resumes IDs
for file in os.listdir(resumeDirectory):

    # create resume ID text
    pdf = FPDF(format="Letter")
    pdf.set_text_color(255,102,102)
    pdf.add_page()
    pdf.set_font("Helvetica", style="B", size=36)
    pdf.set_x(160)
    pdf.cell(0, txt=f"R-{i:04}", ln=1, align="c")
    pdf.output(f"R-{i:04}-ID.pdf")

    # merge resume with ID
    resume          = open(file, "rb")
    resumeReader    = PyPDF2.PdfFileReader(resume)
    resumeP1        = resumeReader.getPage(0)

    resumeID        = open(f"R-{i:04}-ID.pdf", "rb")
    resumeIDreader  = PyPDF2.PdfFileReader(resumeID)

    resumeP1.mergePage(resumeIDreader.getPage(0))

    pdfWriter       = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(resumeP1)

    for pageNum in range(1, resumeReader.numPages):
        pageObj = resumeReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    finalMergedPDF = open(f"R-{i:04}.pdf", "wb")
    pdfWriter.write(finalMergedPDF)

    resume.close()
    resumeID.close()

    os.remove(file)
    os.remove(f"R-{i:04}-ID.pdf")
    

    i+=1