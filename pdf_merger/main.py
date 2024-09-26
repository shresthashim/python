from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

# List all PDF files in the current directory
files = [file for file in os.listdir() if file.endswith('.pdf')]

# Append each PDF file to the merger
for file in files:
    merger.append(file)

# Write the merged PDF to a new file
merger.write('merged.pdf')
merger.close()
