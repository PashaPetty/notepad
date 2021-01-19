import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm
from tkinter.font import Font

file_name = ""

window = tk.Tk()
window.title("блокнот")
window.geometry("500x500")
font = Font(family="Courier", size=10)
file_label = tk.Label(window, text="file: "+file_name)
file_label.place(x=0, y=1, anchor="sw")

def zoom(size):
    font.configure(size=size)

def open_file():
    content.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    file_label["text"] = "file: " + file_name
    with open(file_name, encoding="UTF-8") as file:
        content.insert(1.0, file.read())


def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    file_label["text"] = "file: " + file_name
    file_content = content.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(file_content)

def save_file():
    global file_name
    if file_name == "":
        save_as_file()
    else:
        file_content = content.get(1.0, "end")
        with open(file_name, "w", encoding="UTF-8") as file:
            file.write(file_content)
 
def new_file():
    global file_name
    if tkm.askokcancel("создание нового файла", "несохранённый текст будет удалён"): 
        file_name = ""
        file_label["text"] = "file: " + file_name
        content.delete(1.0, "end")

zoom_scale = tk.Scale(window, orient="vertical", from_=1, to=200)
zoom_scale.config(command=zoom)
text = tk.Text(window, font=font)
zoom_scale.pack(fill="y", side="right")
text.pack(side="left", fill="both", expand=True)
zoom_scale.set(10)

content = tk.Text(window, wrap="word")
content.place(x=0, y=0, width=1, height=1)
main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="файл", menu=file_menu)
new_file_icon = tk.PhotoImage(file="new_file.gif")
file_menu.add_command(label="новый", image=new_file_icon, compound="left", command=new_file)
open_file_icon = tk.PhotoImage(file="open_file.gif")
file_menu.add_command(label="открыть", image=open_file_icon, compound="left", command=open_file)
save_file_icon = tk.PhotoImage(file="save_file.gif")
file_menu.add_command(label="сохранить как", image=save_file_icon, compound="left", command=save_file)
window.mainloop()