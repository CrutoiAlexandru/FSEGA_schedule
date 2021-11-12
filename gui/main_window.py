from tkinter import *
import gui.std_data_window as sdw
import datetime   
import json
import days_of_the_week.monday as monday
import days_of_the_week.tuesday as tuesday
import days_of_the_week.wednesday as wednesday
import days_of_the_week.thursday as thursday
import days_of_the_week.friday as friday
from PIL import Image
from tkinter import messagebox

class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        width = round(Frame.winfo_screenwidth(self)/2)
        height = round(Frame.winfo_screenheight(self)/2)
    
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        enter_class = Button(self, text="Enter class", width = int(width*0.02), height = int(height*0.02), command=self.enter_class)
        enter_class.pack(side = LEFT)

        schedule = Button(self, text="Schedule", width = int(width*0.02), height = int(height*0.02), command=self.show_schedule)
        schedule.pack(side = RIGHT)

        mod_data = Button(self, text="Modify student info", width = int(width*0.02), height = int(height*0.01), command=self.std_data_window)
        mod_data.pack(side = BOTTOM)

    def enter_class(self):
        day = datetime.datetime.today().weekday()

        with open("config.json", "r") as file:
            config = json.load(file)

        if day == 0:
            monday.monday(config["GROUP"], config["LANG"], config["SEMIG"])
        if day == 1:
            tuesday.tuesday(config["GROUP"], config["LANG"], config["SEMIG"])
        if day == 2:
            wednesday.wednesday(config["GROUP"], config["LANG"], config["SEMIG"])
        if day == 3:
            thursday.thursday(config["GROUP"], config["LANG"], config["SEMIG"])
        if day == 4:
            friday.friday(config["GROUP"], config["LANG"], config["SEMIG"])

    def show_schedule(self):
        img = Image.open("img/fsega_schedule.png")
        img.show()

    def std_data_window(self):
        sdw.window()

def noclass():
    messagebox.showinfo(title = "Info", message = "You have no class to attend to right now")

def bad_teacher():
    messagebox.showinfo(title = "Info", message = "Eu nu am optionalul si tanti nu da linkul pe orar csf")

def main_window():
    root = Tk()

    width = round(root.winfo_screenwidth()/2)
    height = round(root.winfo_screenheight()/2)

    app = MainWindow(root)
    root.wm_title("FSEGA Schedule")

    root.geometry(str(0) + 'x' + str(0))
    root.minsize(int(width*0.2)*3, int(width*0.02)*20)

    root.mainloop()