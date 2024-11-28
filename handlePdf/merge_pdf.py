# Python script to glue multiple pdf to one
# To use it, we need to put all .pdf files need to be glued together in a folder operatiion
# Plus this folder need to be in the same folder as this python script
# Build this script just for the sake of some online application which require couple years 
# tax file combined as one and uploaded on government website.
# If you need to glue multip uploaded dile in one. You can easily tailor this script combined 
# with your webservice

from pathlib import Path
from pypdf import PdfWriter

def PDFmerge(pdfs, output):
    # creating pdf file writer object
    pdfWriter = PdfWriter()

    # appending pdfs one by one
    for pdf in pdfs:
        pdfWriter.append(pdf)

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfWriter.write(f)

all_pdf_lst = []
for path in Path("./operation").rglob('*'):  # iterate over all
    if path.suffix.lower() == ".pdf":  # check if the path pattern matches
        all_pdf_lst.append(path)

PDFmerge(all_pdf_lst, "./operation/merged.pdf")
