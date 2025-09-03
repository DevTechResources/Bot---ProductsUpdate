import customtkinter as ctk
from PIL import Image

class Card(ctk.CTkFrame):
    def __init__(self, master, iconImage, title, description, destino):
        super().__init__(master)

        self.configure(fg_color="white", border_width=2, border_color="#7B7B7B", corner_radius=28)

        #Crear los iconos
        iconCard = ctk.CTkImage(light_image=Image.open(iconImage), size=(61, 61))
        iconButton = ctk.CTkImage(light_image=Image.open("images/right-arrow.png"), size=(28, 28))

        #Colores
        colorButton="#152645"
        colorHover="#1F3867"
        
        #Crear frame para el contenido de la tarjeta
        frameContenido = ctk.CTkFrame(self, fg_color="transparent")
        ##Crear los componentes para el frame de Contenido
        ctk.CTkLabel(frameContenido, text="", image=iconCard, text_color="black").grid(row=0, column=0) 
        ctk.CTkLabel(frameContenido, text=title, text_color="black", font=("Roboto",24, "bold")).grid(row=1, column=0) 
        ctk.CTkLabel(frameContenido, text=description, text_color="black", font=("Roboto",16)).grid(row=2, column=0) 
        
        ##Configurar la posicion del frame de contenidos respecto a la card
        frameContenido.grid(row=0, column=0, rowspan=3, sticky="n"+"w"+"e"+"s", pady=(20,0), padx=20)
        ##Configurar las filas para que crezcan proporcionalmente 
        frameContenido.grid_rowconfigure(list(range(3)), weight = 1)
        ##Configurar las columnas para que crezcan proporcionalmente 
        frameContenido.grid_columnconfigure(0, weight=1)

        #Crear frame para el botón de la tarjeta
        frameButton = ctk.CTkFrame(self, fg_color="transparent")
        ##Crear los componentes para el frame de Contenido
        ctk.CTkButton(frameButton,
            corner_radius=15,
            width=28,
            border_spacing=16,
            text="",
            image=iconButton, 
            fg_color=colorButton,
            hover_color=colorHover
            ).grid(row=0, column=0) 

        ##Configurar la posicion del frame del botón respecto a la card
        frameButton.grid(row=3, column=0, sticky="n"+"w"+"e"+"s", pady=(0,20), padx=20)
        # Configurar las filas para que crezcan proporcionalmente 
        frameButton.grid_rowconfigure(0, weight = 1)
        # Configurar las columnas para que crezcan proporcionalmente 
        frameButton.grid_columnconfigure(0, weight=1)
        

        # Configurar las filas de la card para que crezcan proporcionalmente 
        self.grid_rowconfigure(list(range(4)), weight = 1)
        # Configurar las columnas de la card para que crezcan proporcionalmente 
        self.grid_columnconfigure(0, weight=1)