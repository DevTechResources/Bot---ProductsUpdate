import customtkinter as ctk
import style.colors as colors
from PIL import Image
from controller.pagesController import PagesController

class TitleBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color=colors.CompanyColor2, corner_radius=0)

        companyLogo= ctk.CTkImage(light_image=Image.open("images/TechResourcesBanner.webp"), size=(352, 60))

        companyLogoLabel = ctk.CTkLabel(self, image=companyLogo, text="")
        companyLogoLabel.pack(fill="x", expand=True, ipady=15)

        controller = PagesController()
        ctk.CTkButton(self, text="Ir", command=lambda: controller.show_frame("UploadPage")).pack()