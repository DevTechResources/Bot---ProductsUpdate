import tkinter as tk
from PIL import Image
from component.titleBar import TitleBar
from pages.homePage import HomePage

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
        frame2 = HomePage(self)
        frame2.pack(expand=True, fill = "both")

app = App()
app.mainloop()