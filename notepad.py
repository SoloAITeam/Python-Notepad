import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import tkinter.font as font

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Notepad")
  
        # Specify the default font names
        self.font_name = "Times New Roman"
        self.font_size = 12
        
        # Load the default font
        self.custom_font = font.Font(family=self.font_name, size=self.font_size)
        
        # Create the text area with the default font
        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, font=self.custom_font, width=60, height=20)
        self.text_area.pack(expand=True, fill='both')

        # Create the menu bar
        self.menu_bar = tk.Menu(master)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Language menu
        self.language_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.language_menu.add_command(label="English", command=lambda: self.set_language("English"))
        self.language_menu.add_command(label="Spanish", command=lambda: self.set_language("Spanish"))
        self.language_menu.add_command(label="French", command=lambda: self.set_language("French"))
        self.menu_bar.add_cascade(label="Language", menu=self.language_menu)
        
        # Fonts menu
        self.fonts_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.fonts_menu.add_command(label="Times New Roman", command=lambda: self.set_font("Times New Roman"))
        self.fonts_menu.add_command(label="Arial", command=lambda: self.set_font("Arial"))
        self.fonts_menu.add_command(label="Courier New", command=lambda: self.set_font("Courier New"))
        self.fonts_menu.add_command(label="Georgia", command=lambda: self.set_font("Georgia"))
        self.menu_bar.add_cascade(label="Fonts", menu=self.fonts_menu)
        
        # Configure the menu bar
        self.master.config(menu=self.menu_bar)
        
        # Disable window resizing
        self.master.resizable(False, False)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file:\n{e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")

    def set_language(self, language):
        messagebox.showinfo("Language", f"Language set to {language}")

    def set_font(self, font_name):
        self.font_name = font_name
        self.custom_font = font.Font(family=self.font_name, size=self.font_size)
        self.text_area.config(font=self.custom_font)

    def exit_app(self):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
