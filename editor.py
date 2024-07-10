import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.filename = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.root.title("Simple Text Editor - New File")

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")]
        )
        if self.filename:
            with open(self.filename, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, file.read())
            self.root.title(f"Simple Text Editor - {self.filename}")

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"Simple Text Editor - {self.filename}")
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")]
        )
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"Simple Text Editor - {self.filename}")

    def exit_editor(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleEditor(root)
    root.mainloop()
