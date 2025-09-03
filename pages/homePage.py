import customtkinter as ctk
from component.homeCards import HomeCards
from component.presentationCard import PresentationCard

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        companyColorWhite = "#F3F1F1"
        self.configure(fg_color=companyColorWhite, corner_radius=0)
        
        # Añadir frames a la homePage
        PresentationCard(self).pack(side="top",fill="x", pady=(30,22))

        #Añadir frame donde salen las tarjetas
        HomeCards(self).pack(expand=True, fill = "both", pady=(22,30))
        