import customtkinter as ctk
import style.colors as colors


class UploadPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="black", corner_radius=0)
        ctk.CTkLabel(self, text="Hola").pack()