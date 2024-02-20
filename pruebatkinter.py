import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import cv2

# Crear la conexión a la base de datos
conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
''')

conn.commit()
conn.close()

def do_login():
    entered_username = entry_username.get()
    entered_password = entry_password.get()

    if entered_username and entered_password:
        # Verificar las credenciales en la base de datos
        conn = sqlite3.connect("user_data.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (entered_username, entered_password))
        user = cursor.fetchone()

        conn.close()

        if user:
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login", "Invalid username or password.")
    else:
        messagebox.showerror("Login", "Username and password are required!")
''''''
def open_register_window():
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    def do_register():
        new_username = register_entry_username.get()
        new_password = register_entry_password.get()

        if new_username and new_password:
            # Guardar los datos en la base de datos
            conn = sqlite3.connect("user_data.db")  # Crear o conectar a la base de datos
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
            conn.commit()
            conn.close()

            messagebox.showinfo("Register", "Registration successful!")
            register_window.destroy()
        else:
            messagebox.showerror("Register", "Username and password are required!")

    register_label_username = ttk.Label(register_window, text="Username")
    register_label_password = ttk.Label(register_window, text="Password")
    register_entry_username = ttk.Entry(register_window)
    register_entry_password = ttk.Entry(register_window, show="*")
    register_button = ttk.Button(register_window, text="Register", command=do_register)

    register_label_username.pack(pady=5)
    register_entry_username.pack(pady=5)
    register_label_password.pack(pady=5)
    register_entry_password.pack(pady=5)
    register_button.pack(pady=10)
# Crear la ventana principal
root = tk.Tk()
root.title("Project 1")

# Establecer las dimensiones iniciales de la ventana
root.geometry("1080x720")

# Estilo colorido y moderno
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#ff5733", padding=10)
style.map("TButton", foreground=[("active", "white")], background=[("active", "#ff8c66")])

# Cargar la imagen y obtener sus dimensiones
image_path = "icono.png"  # Cambiar la ruta a tu imagen
original_image = Image.open(image_path)
image_width, image_height = original_image.size

# Calcular el nuevo tamaño de la imagen manteniendo la relación de aspecto
new_width = 600
new_height = int((new_width / image_width) * image_height)
resized_image = original_image.resize((new_width, new_height))
image = ImageTk.PhotoImage(resized_image)

# Crear etiqueta de imagen en la mitad izquierda
image_label = ttk.Label(root, image=image)
image_label.grid(row=0, column=0, padx=20, pady=20, rowspan=3, sticky="nsew")

# Crear marco en la mitad derecha para los botones
button_frame = ttk.Frame(root)
button_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Crear cuadros de texto para el login con estilo
style.configure("TLabel", font=("Helvetica", 16))  # Estilo para las etiquetas
style.configure("TEntry", font=("Helvetica", 16))  # Estilo para las cajas de texto

label_username = ttk.Label(button_frame, text="Username")
label_password = ttk.Label(button_frame, text="Password")
entry_username = ttk.Entry(button_frame, style="TEntry")
entry_password = ttk.Entry(button_frame, show="*", style="TEntry")

label_username.pack(pady=10)
entry_username.pack(pady=10)
label_password.pack(pady=10)
entry_password.pack(pady=10)

# Crear botones en el marco con estilo
login_button = ttk.Button(button_frame, text="Login", command=do_login, style="TButton")
register_button = ttk.Button(button_frame, text="Register", command=open_register_window, style="TButton")

login_button.pack(pady=20, fill="x")
register_button.pack(pady=10, fill="x")

# Configurar pesos para que los elementos se adapten a la ventana
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_rowconfigure(1, weight=1)
button_frame.grid_rowconfigure(2, weight=1)
button_frame.grid_rowconfigure(3, weight=1)
button_frame.grid_rowconfigure(4, weight=1)  # Agregado para los botones

# Iniciar el bucle de eventos
root.mainloop()
