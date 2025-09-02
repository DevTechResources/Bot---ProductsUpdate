import customtkinter as ctk
from component.homeCards import HomeCards

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        companyColorWhite = "#F3F1F1"
        self.configure(fg_color=companyColorWhite, corner_radius=0)
        
        # Añadir frames al grid 
        framePresentation = ctk.CTkFrame(self, fg_color="purple", corner_radius=0)
        framePresentation.grid(row=0, column=0, sticky='w'+'e'+'n'+'s', pady=22) 
        
        #Añadir frame donde salen las tarjetas
        frameCards = HomeCards(self)
        frameCards.grid(row=1, column=0, sticky='w'+'e'+'n'+'s', rowspan=2, pady=22) 

        # Configurar las columnas para que crezcan proporcionalmente 
        self.grid_columnconfigure(0, weight=1) 

        # Configurar las filas para que crezcan proporcionalmente 
        self.grid_rowconfigure(list(range(3)), weight = 1, uniform="Silent_Creme")