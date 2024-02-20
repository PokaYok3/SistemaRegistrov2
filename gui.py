import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from database import DatabaseManager

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1080x720")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", foreground="white", background="#ff5733", padding=10)
        self.style.map("TButton", foreground=[("active", "white")], background=[("active", "#ff8c66")])

        self.database_manager = DatabaseManager("user_data.db")
        self.create_ui()

    def do_login(self):
        entered_username = self.entry_username.get()
        entered_password = self.entry_password.get()

        if entered_username and entered_password:
            user = self.database_manager.verify_credentials(entered_username, entered_password)
            if user:
                messagebox.showinfo("Login", "Login successful!")
            else:
                messagebox.showerror("Login", "Invalid username or password.")
        else:
            messagebox.showerror("Login", "Username and password are required!")

    def open_register_window(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register")

        def do_register():
            new_username = register_entry_username.get()
            new_password = register_entry_password.get()

            if new_username and new_password:
                self.database_manager.insert_user(new_username, new_password)
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

    def create_ui(self):
        image_path = "icono.png"
        original_image = Image.open(image_path)
        image_width, image_height = original_image.size
        new_width = 600
        new_height = int((new_width / image_width) * image_height)
        resized_image = original_image.resize((new_width, new_height))
        self.image = ImageTk.PhotoImage(resized_image)

        image_label = ttk.Label(self.root, image=self.image)
        image_label.grid(row=0, column=0, padx=20, pady=20, rowspan=3, sticky="nsew")

        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        login_button = ttk.Button(button_frame, text="Login", command=self.do_login, style="TButton")
        register_button = ttk.Button(button_frame, text="Register", command=self.open_register_window, style="TButton")

        login_button.pack(pady=20, fill="x")
        register_button.pack(pady=10, fill="x")

        label_username = ttk.Label(button_frame, text="Username")
        label_password = ttk.Label(button_frame, text="Password")
        self.entry_username = ttk.Entry(button_frame, style="TEntry")
        self.entry_password = ttk.Entry(button_frame, show="*", style="TEntry")

        label_username.pack(pady=10)
        self.entry_username.pack(pady=10)
        label_password.pack(pady=10)
        self.entry_password.pack(pady=10)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)
        button_frame.grid_rowconfigure(2, weight=1)
        button_frame.grid_rowconfigure(3, weight=1)
        button_frame.grid_rowconfigure(4, weight=1)

