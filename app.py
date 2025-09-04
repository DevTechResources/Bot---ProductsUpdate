import tkinter as tk
import customtkinter as ctk
from PIL import Image
from component.titleBar import TitleBar
from controller.pagesController import PagesController

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Window aspect configuration
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f"{screenWidth}x{screenHeight}+0+0")
        self.state("zoomed")
        self.title("CTk example")

        #Frame for the title bar
        frame1 = TitleBar(self)
        frame1.pack(side="top",fill="x")

        #Frame for the HomePage
        frame2 = ctk.CTkFrame(self, fg_color="pink")
        frame2.pack(expand=True, fill = "both")
        

        #Create the pageController
        controller = PagesController()
        controller.establishPageContainer(frame2)


app = App()
app.mainloop()