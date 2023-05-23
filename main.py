import tkinter as tk
from tkinter import filedialog as fd
from transformers import pipeline


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

button = tk.Button(root, text="Summarize", command=summarize)
button.pack()
button['cursor'] = 'cross'

result_label = tk.Label(root, text="Summary:")
result_label.pack()

result_text = tk.Text(root, wrap=tk.WORD)
result_text.pack()

save_button = tk.Button(root, text="Save Summary", command=save_summary)
save_button.pack()
save_button['cursor'] = 'cross'

root.mainloop()
