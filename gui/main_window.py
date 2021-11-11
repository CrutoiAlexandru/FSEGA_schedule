from tkinter import *

class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        width = round(Frame.winfo_screenwidth(self)/2)
        height = round(Frame.winfo_screenheight(self)/2)
    
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", width = int(width*0.02), height = int(height*0.02), command=self.std_data_window)

        # place button at (0,0)
        exitButton.pack(side = LEFT, padx = int(width*0.1))

        secondButton = Button(self, text="Second button", width = int(width*0.02), height = int(height*0.02), command=self.clickExitButton)

        secondButton.pack(side = RIGHT, padx = int(width*0.1))

    def clickExitButton(self):
        exit()

    def std_data_window(self):
        root = Tk()

        width = str(round(root.winfo_screenwidth()/2))
        height = str(round(root.winfo_screenheight()/2))

        app = MainWindow(root)
        root.wm_title("Tkinter button")

        root.geometry(width + 'x' + height)

        root.mainloop()
        
def main_window():
    root = Tk()

    width = str(round(root.winfo_screenwidth()/2))
    height = str(round(root.winfo_screenheight()/2))

    app = MainWindow(root)
    root.wm_title("Tkinter button")

    root.geometry(width + 'x' + height)

    root.mainloop()