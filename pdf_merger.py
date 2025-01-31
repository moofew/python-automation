import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir): 
    if file.endswith(".pdf"):
        print(file)
        merger = PyPDF2.PdfFileMerger()
        merger.append(file)
    merger.write("combinedPDF.pdf")