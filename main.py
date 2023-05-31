import tkinter as tk
from tkinter import filedialog as fd
from transformers import pipeline
import pdf_extract as pd


def split_text(text, max_length):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]


def summarize():
    summarizer = pipeline('summarization')
    article = input_text.get("1.0", tk.END)
    max_length = 1024
    parts = split_text(article, max_length)
    summary = ""
    for part in parts:
        result = summarizer(part, max_length=130,
                            min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + "\n"
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, summary)


def save_summary():
    file = fd.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        text_to_save = result_text.get("1.0", tk.END)
        file.write(text_to_save)
        file.close()


root = tk.Tk()
root.title("Hugging face based Summarizer")

input_label = tk.Label(root, text="Paste article:")
input_label.pack()
input_text = tk.Text(root)
input_text.pack()

#Button Canvas
button_can = tk.Canvas(root)
button_can.pack()

#______PdfSelction_Button___________
def inserttext() :
    pdf_text = pd.select_file()
    global input_text
    input_text.insert(tk.END,pdf_text)
    


button_pdf= tk.Button(button_can, text="Select Pdf",width=20, command=inserttext)
button_pdf.grid(row=0,column=0,sticky='W',padx=30)
button_pdf['cursor'] = 'cross'

#______Summarize_Button___________
button_Summarize = tk.Button(button_can, text="Summarize",width=20, command=summarize)
button_Summarize.grid(row=0,column=1,padx=30)
button_Summarize['cursor'] = 'cross'

#______Clear_Button___________
def clear_inputtext() :
    input_text.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)

button_clear = tk.Button(button_can, text="Clear",width=20, command=clear_inputtext)
button_clear.grid(row=0,column=3,padx=30,sticky='E')
button_clear['cursor'] = 'cross'

result_label = tk.Label(root, text="Summary:")
result_label.pack()

result_text = tk.Text(root, wrap=tk.WORD)
result_text.pack()

save_button = tk.Button(root, text="Save Summary", command=save_summary)
save_button.pack()
save_button['cursor'] = 'cross'

root.mainloop()
