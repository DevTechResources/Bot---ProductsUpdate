import customtkinter as ctk
from component.customCTkButton import CustomCTkButton
from PIL import Image
import style.colors as colors

class PageChangerButtons(ctk.CTkFrame):
    def __init__(self, master, textButton1, textButton2, destinyButton1, destinyButton2):
        super().__init__(master, fg_color="transparent")
        
        #Importar el controlador de paginas
        from controller.pagesController import PagesController
        controller = PagesController()

        #Crear los iconos
        iconBack = ctk.CTkImage(light_image=Image.open("images/left-arrow.png"), size=(10.97, 19.41))
        iconProceed = ctk.CTkImage(light_image=Image.open("images/check-mark.png"), size=(24, 24))
        
        #Botón para ir atrás
        CustomCTkButton(self,
            image = iconBack,
            text = textButton1,
            height = 60,
            corner_radius = 15,
            fg_color = colors.CompanyColor1,
            hover_color = colors.CompanyColor1Variant1,
            compound = "left",
            command = lambda: controller.show_frame(destinyButton1),
            font = ("Roboto",18)
            ).pack(side="left")
        
        #Botón para avanzar
        CustomCTkButton(self,
            image=iconProceed,
            text=textButton2,
            height=60,
            corner_radius = 15,
            fg_color=colors.CompanyColor1,
            hover_color=colors.CompanyColor1Variant1,
            compound="right",
            command=lambda: controller.show_frame(destinyButton2),
            font = ("Roboto",18)
            ).pack(side="right")