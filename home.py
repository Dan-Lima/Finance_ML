from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from math import *
from scipy.stats import norm
import option_pricer as op
import machine_learning as ml

#runs when MainWindow is closed
def MainWindowClosed(Window):
	Window.quit()
	Window.destroy()

#Main function
if __name__ == '__main__':
	#Creates main window
	MainWindow=Tk()
	MainWindow.config(bg="gray10")
	MainWindow.geometry("600x600")
	MainWindow.protocol("WM_DELETE_WINDOW", lambda arg=MainWindow: MainWindowClosed(arg))

	#Designs main window
	MainFrame=Frame(MainWindow, bg="gray10")
	MainFrame.grid(row=0, column=0)
	
	Button_OptionPricer = Button(MainFrame,text="Options Pricer",command=op.OptionPricer, bg="gray25", fg="gray99", anchor=W)
	Button_OptionPricer.grid(row=0, column=0, padx=5, pady=5, sticky=W)
	
	Button_MachineLearning = Button(MainFrame,text="Machine Learning",command=ml.MachineLearning, bg="gray25", fg="gray99", anchor=W)
	Button_MachineLearning.grid(row=1, column=0, padx=5, pady=5, sticky=W)

	MainWindow.mainloop()