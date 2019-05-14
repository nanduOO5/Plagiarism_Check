import tkinter
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename
from difflib import SequenceMatcher

class GUI:

    def __init__(self, window): 
        # 'StringVar()' is used to get the instance of input field
        self.input_text = StringVar()
        self.input_text1 = StringVar()
        self.res = StringVar()
        self.path = ''
        self.path1 = ''

        window.title("Plagiarism Checker")
        window.resizable(0, 0) # this prevents from resizing the window
        window.geometry("700x300")

        ttk.Entry(window, textvariable = self.input_text, width = 70).grid( row = 0, column = 0, ipadx=1, ipady=1) # this is placed in 0 1
        ttk.Button(window, text = "File", command = lambda: self.set_path_File_field()).grid(row = 0, column=1, ipadx=5, ipady=15) # this is placed in 0 0

        ttk.Entry(window, textvariable = self.input_text1, width = 70).grid( row = 1, column = 0, ipadx=1, ipady=1) # this is placed in 0 1
        ttk.Button(window, text = "Reference File", command = lambda: self.set_path_Base_field()).grid(row = 1, column=1, ipadx=5, ipady=15) # this is placed in 0 0

        ttk.Button(window, text = "Check", command = lambda: self.check()).grid(row = 2, ipadx=5, ipady=15) # this is placed in 0 0
   
    def set_path_File_field(self):
        self.path = askopenfilename() 
        self.input_text.set(self.path)

    def set_path_Base_field(self):
        self.path1 = askopenfilename()
        self.input_text1.set(self.path1)

    def getFilePath(self): 
        """ Function provides the Users full file path."""
        return self.path

    def getBasePath(self):
        """Function provides the Enova full file path."""
        return self.path1

    def check(self):
        self.file1=self.getFilePath()
        self.file2=self.getBasePath()
        with open(self.file1) as f1,open(self.file2) as f2:
            self.f1_data=f1.read()
            self.f2_data=f2.read()
            self.res = SequenceMatcher(None,self.f1_data,self.f2_data).ratio()
            popup=tkinter.Tk()
            popup.wm_title("Difference Ratio")
            label=ttk.Label(popup,text=self.res)
            label.pack()
            popup.mainloop()

if __name__ == '__main__':
    window = tkinter.Tk()
    gui = GUI(window)
    window.mainloop()
