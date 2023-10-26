import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import subprocess

def browse_script():
    script_file = filedialog.askopenfilename(filetypes=[("C Files", "*.c")])
    script_entry.delete(0, tk.END)
    script_entry.insert(0, script_file)

def compile_script():
    script_file = script_entry.get()
    if script_file:
        progress_window = tk.Toplevel(app)
        progress_window.title("Compilation Progress")
        progress_text = ScrolledText(progress_window, wrap=tk.WORD, height=20, width=50)
        progress_text.pack()
        
        def compile():
            cmd = ['pyinstaller', '--onefile', script_file]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            while True:
                output = process.stdout.readline()
                if not output:
                    break
                progress_text.insert(tk.END, output)
                progress_text.see(tk.END)
        
        progress_button = ttk.Button(progress_window, text="Compile", command=compile)
        progress_button.pack()
        compile()

def compile_c():
    c_file = script_entry.get()
    if c_file.endswith('.c'):
        progress_window = tk.Toplevel(app)
        progress_window.title("Compilation Progress")
        progress_text = ScrolledText(progress_window, wrap=tk.WORD, height=20, width=50)
        progress_text.pack()
        
        def compilec():
            cmd = ['cl', c_file]  # Use 'cl' for Microsoft's C/C++ compiler
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            while True:
                output = process.stdout.readline()
                if not output:
                    break
                progress_text.insert(tk.END, output)
                progress_text.see(tk.END)
        
        progress_button = ttk.Button(progress_window, text="Compile C", command=compilec)
        progress_button.pack()
        compilec()

def copy():
    script_entry.event_generate("<<Copy>>")

def paste():
    script_entry.event_generate("<<Paste>>")

def cut():
    script_entry.event_generate("<<Cut>>")

app = tk.Tk()
app.title("EXEpy v1.0.0")

# Create a frame for the content
content_frame = ttk.Frame(app, padding=10)
content_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Configure row and column weights to make the layout expand properly
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

# Disable maximizing and set a fixed window size
app.geometry('600x400')  # Set the desired window size
app.resizable(0, 0)

# Create the elements and arrange them in sections
script_label = ttk.Label(content_frame, text="Select a C File or Path:")
script_label.grid(column=0, row=0, sticky=tk.W)

script_entry = ttk.Entry(content_frame, width=50)
script_entry.grid(column=0, row=1, padx=10, sticky=tk.W)

browse_button = ttk.Button(content_frame, text="Browse", command=browse_script)
browse_button.grid(column=1, row=1, sticky=tk.W)

separator = ttk.Separator(content_frame, orient='horizontal')
separator.grid(column=0, row=2, columnspan=2, pady=10, sticky=(tk.W, tk.E))

compile_button = ttk.Button(content_frame, text="Compile/ .EXE", command=compile_c)
compile_button.grid(column=0, row=3, pady=10, sticky=tk.W)

result_label = ttk.Label(content_frame, text="", foreground="green")
result_label.grid(column=0, row=4, columnspan=2, pady=5, sticky=tk.W)

# Create a Menu bar
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

# Create File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Browse", command=browse_script)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Create Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

app.mainloop()
