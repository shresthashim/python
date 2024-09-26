from PyPDF2 import PdfMerger
import os

# Custom sort key to extract the number part of the filename
def sort_key(file):
    # Split the filename by '-' and '.pdf' to extract the number
    return int(file.split('-')[1].split('.')[0])

merger = PdfMerger()

# List all PDF files in the current directory and sort them
files = sorted([file for file in os.listdir() if file.endswith('.pdf')], key=sort_key)

# Append each sorted PDF file to the merger
for file in files:
    merger.append(file)

# Write the merged PDF to a new file
merger.write('merged.pdf')
merger.close()
