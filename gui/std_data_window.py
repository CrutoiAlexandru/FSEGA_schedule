from tkinter import *
import coms
import time

gr1 = Button
class StdDataWindow(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        width = round(Frame.winfo_screenwidth(self)/2)
        height = round(Frame.winfo_screenheight(self)/2)
    
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        #choose your group
        group_label = Label(self, text="Group:")
        group_label.grid(row = 0, column = 0)

        gr1 = Button(self, text="1", width = int(width*0.01), height = int(height*0.01), command = self.group1)
        gr1.grid(row = 0, column = 1)

        gr2 = Button(self, text="2", width = int(width*0.01), height = int(height*0.01), command = self.group2)
        gr2.grid(row = 0, column = 2)

        gr3 = Button(self, text="3", width = int(width*0.01), height = int(height*0.01), command = self.group3)
        gr3.grid(row = 0, column = 3)

        gr4 = Button(self, text="4", width = int(width*0.01), height = int(height*0.01), command = self.group4)
        gr4.grid(row = 0, column = 4)

        gr5 = Button(self, text="5", width = int(width*0.01), height = int(height*0.01), command = self.group5)
        gr5.grid(row = 0, column = 5)

        #choose your language
        group_label = Label(self, text="Language:")
        group_label.grid(row = 2, column = 0)

        language1 = Button(self, text="English", width = int(width*0.01), height = int(height*0.01), command = self.lang1)
        language1.grid(row = 2, column = 1)

        language2 = Button(self, text="German", width = int(width*0.01), height = int(height*0.01), command = self.lang2)
        language2.grid(row = 2, column = 2)

        language3 = Button(self, text="Italian", width = int(width*0.01), height = int(height*0.01), command = self.lang3)
        language3.grid(row = 2, column = 3)

        language4 = Button(self, text="French", width = int(width*0.01), height = int(height*0.01), command = self.lang4)
        language4.grid(row = 2, column = 4)

        language5 = Button(self, text="Spanish", width = int(width*0.01), height = int(height*0.01), command = self.lang5)
        language5.grid(row = 2, column = 5)

        #choose your semigroup
        group_label = Label(self, text="Semigroup:")
        group_label.grid(row = 4, column = 0)

        semig1 = Button(self, text="1", width = int(width*0.01), height = int(height*0.01), command = self.semig1)
        semig1.grid(row = 4, column = 1)

        semig2 = Button(self, text="2", width = int(width*0.01), height = int(height*0.01), command = self.semig2)
        semig2.grid(row = 4, column = 2)

        #choose your optional classes
        #only the ones that need management
        #support for only one classes
        opt_label = Label(self, text="Optional:")
        opt_label.grid(row = 6, column = 0)

        opt1 = Button(self, text="Doctrine", width = int(width*0.01), height = int(height*0.01), command = self.opt1)
        opt1.grid(row = 6, column = 1)

        opt2 = Button(self, text="Management", width = int(width*0.01), height = int(height*0.01), command = self.opt2)
        opt2.grid(row = 6, column = 2)

        opt3 = Button(self, text="Fiscalitate", width = int(width*0.01), height = int(height*0.01), command = self.opt3)
        opt3.grid(row = 6, column = 3)

        opt4 = Button(self, text="Other", width = int(width*0.01), height = int(height*0.01), command = self.opt4)
        opt4.grid(row = 6, column = 4)

    def group1(self):
        coms.std_group(1)

        lbl = Label(self, text="Group: 1")
        lbl.grid(row = 1, column = 1)
        
    def group2(self):
        coms.std_group(2)

        lbl = Label(self, text="Group: 2")
        lbl.grid(row = 1, column = 1)

    def group3(self):
        coms.std_group(3)

        lbl = Label(self, text="Group: 3")
        lbl.grid(row = 1, column = 1)

    def group4(self):
        coms.std_group(4)

        lbl = Label(self, text="Group: 4")
        lbl.grid(row = 1, column = 1)

    def group5(self):
        coms.std_group(5)

        lbl = Label(self, text="Group: 5")
        lbl.grid(row = 1, column = 1)

    def lang1(self):
        coms.std_lang(1)

        lbl = Label(self, text="Language: English")
        lbl.grid(row = 3, column = 1)

    def lang2(self):
        coms.std_lang(2)

        lbl = Label(self, text="Language: German")
        lbl.grid(row = 3, column = 1)

    def lang3(self):
        coms.std_lang(3)

        lbl = Label(self, text="Language: Italian")
        lbl.grid(row = 3, column = 1)

    def lang4(self):
        coms.std_lang(4)

        lbl = Label(self, text="Language: French")
        lbl.grid(row = 3, column = 1)

    def lang5(self):
        coms.std_lang(5)

        lbl = Label(self, text="Language: Spanish")
        lbl.grid(row = 3, column = 1)

    def semig1(self):
        coms.std_semig(1)

        lbl = Label(self, text="Semigroup: 1")
        lbl.grid(row = 5, column = 1)

    def semig2(self):
        coms.std_semig(2)

        lbl = Label(self, text="Semigroup: 2")
        lbl.grid(row = 5, column = 1)

    def opt1(self):
        coms.std_optional(1)

        lbl = Label(self, text="Optional: Doctrine")
        lbl.grid(row = 7, column = 1)

    def opt2(self):
        coms.std_optional(2)

        lbl = Label(self, text="Optional: Management")
        lbl.grid(row = 7, column = 1)

    def opt3(self):
        coms.std_optional(3)

        lbl = Label(self, text="Optional: Fiscalitate")
        lbl.grid(row = 7, column = 1)

    def opt4(self):
        coms.std_optional(4)

        lbl = Label(self, text="Optional: Other")
        lbl.grid(row = 7, column = 1)
        
def window():
    root = Tk()

    width = round(root.winfo_screenwidth()/2)
    height = round(root.winfo_screenheight()/2)

    app = StdDataWindow(root)
    root.wm_title("Student info")

    # root.geometry(str(0) + 'x' + str(0))
    root.grid_columnconfigure((0, 1), weight = 1)
    root.minsize(int(width*0.22)*3, int(width*0.02)*25)
    root.maxsize(int(width*0.22)*3, int(width*0.02)*25)

    root.mainloop()