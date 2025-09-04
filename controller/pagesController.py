from controller.singletonMeta import SingletonMeta
from pages.homePage import HomePage
from pages.uploadPage import UploadPage

class PagesController(metaclass=SingletonMeta):
    def establishPageContainer(self, container):
        self.container = container
        self.frames = {}
        for F in (HomePage, UploadPage):
            page_name = F.__name__
            frame = F(self.container)
            self.frames[page_name] = frame

            frame.grid(column=0, row=0, sticky="n"+"s"+"e"+"w")
            
        # Configurar las filas de la card para que crezcan proporcionalmente 
        self.container.grid_rowconfigure(0, weight = 1, uniform="Silent_Creme")
        # Configurar las columnas de la card para que crezcan proporcionalmente 
        self.container.grid_columnconfigure(0, weight=1, uniform="Silent_Creme")

        self.show_frame("HomePage")
        print(self.frames)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        print(frame)
        frame.lift()