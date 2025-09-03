import customtkinter as ctk
from PIL import Image

class PresentationCard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="transparent")

        # Añadir elementos a la card
        icon = ctk.CTkImage(light_image=Image.open("images/robot.png"), size=(80, 80))

        ctk.CTkLabel(self, image= icon, text="").grid(row=0, column=0) 
        ctk.CTkLabel(self,
            text="Bot de actualización de productos",
            text_color="black",
            font=("Roboto",32, "bold"),
            pady=10
        ).grid(row=1, column=0) 
        ctk.CTkLabel(self,
            text="Bienvenido al bot de actualización del catálogo de productos de la tienda online. "
            "Selecciona una de las opciones a continuación para \ncomenzar.",
            text_color="black",
            font=("Roboto",20)
        ).grid(row=2, column=0)
        
        # Configurar las filas para que crezcan proporcionalmente 
        self.grid_rowconfigure(list(range(3)), weight = 1)

        # Configurar las columnas para que crezcan proporcionalmente 
        self.grid_columnconfigure(0, weight=1)