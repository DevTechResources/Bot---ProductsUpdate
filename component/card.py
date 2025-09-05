import customtkinter as ctk
import style.colors as colors
from PIL import Image
from component.customCTkButton import CustomCTkButton

class Card(ctk.CTkFrame):
    def __init__(self, master, iconImage, title, description, destiny):
        super().__init__(master, fg_color="transparent")

        frameShadow = ctk.CTkFrame(self, border_width=0, fg_color='#d1cfcf', corner_radius=28)
        frameShadow.grid(row=0, column=0, sticky='n'+'s'+'w'+'e')
        
        frameTarjeta = ctk.CTkFrame(self, fg_color="white", border_width=2, border_color="#7B7B7B", corner_radius=15)
        frameTarjeta.grid(row=0, column=0, sticky='n'+'s'+'w'+'e', pady=(0,5), padx=(0,5))

        # # Configurar las filas de la card para que crezcan proporcionalmente 
        self.grid_rowconfigure(0, weight = 1)
        # # Configurar las columnas de la card para que crezcan proporcionalmente 
        self.grid_columnconfigure(0, weight=1)

        #Crear los iconos
        iconCard = ctk.CTkImage(light_image=Image.open(iconImage), size=(61, 61))
        iconButton = ctk.CTkImage(light_image=Image.open("images/right-arrow.png"), size=(28, 28))
        
        #Crear frame para el contenido de la tarjeta
        frameContenido = ctk.CTkFrame(frameTarjeta, fg_color="transparent")
        ##Crear los componentes para el frame de Contenido
        ctk.CTkLabel(frameContenido, text="", image=iconCard, text_color="black").grid(row=0, column=0) 
        ctk.CTkLabel(frameContenido, text=title, text_color="black", font=("Roboto",24, "bold")).grid(row=1, column=0) 
        ctk.CTkLabel(frameContenido, text=description, text_color="black", font=("Roboto",18)).grid(row=2, column=0) 
        
        ##Configurar la posicion del frame de contenidos respecto a la card
        frameContenido.grid(row=0, column=0, rowspan=3, sticky="n"+"w"+"e"+"s", pady=(20,0), padx=20)
        ##Configurar las filas para que crezcan proporcionalmente 
        frameContenido.grid_rowconfigure(list(range(3)), weight = 1)
        ##Configurar las columnas para que crezcan proporcionalmente 
        frameContenido.grid_columnconfigure(0, weight=1)

        #Crear frame para el botón de la tarjeta
        frameButton = ctk.CTkFrame(frameTarjeta, fg_color="transparent")
        
        ##Crear los componentes para el frame del botón
        from controller.pagesController import PagesController
        controller = PagesController()
        CustomCTkButton(frameButton,
            image=iconButton,
            text="",
            height=60,
            width=60,
            corner_radius = 15,
            fg_color=colors.CompanyColor1,
            hover_color=colors.CompanyColor1Variant1,
            command=lambda: controller.show_frame(destiny)
            ).grid(row=0,column=0)

        ##Configurar la posicion del frame del botón respecto a la card
        frameButton.grid(row=3, column=0, pady=(0,15), padx=(20, 15))
        # Configurar las filas para que crezcan proporcionalmente 
        frameButton.grid_rowconfigure(0, weight = 1)
        # Configurar las columnas para que crezcan proporcionalmente 
        frameButton.grid_columnconfigure(0, weight=1)

        # Configurar las filas de la card para que crezcan proporcionalmente 
        frameTarjeta.grid_rowconfigure(list(range(4)), weight = 1)
        # Configurar las columnas de la card para que crezcan proporcionalmente 
        frameTarjeta.grid_columnconfigure(0, weight=1)