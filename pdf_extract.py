from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
# File Selection 
def select_file():
    filetypes = (
        ('Pdf files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='../',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    
    if filename != '' :
        reader = PdfReader(filename)
        page = reader.pages[0]
        return(page.extract_text())



