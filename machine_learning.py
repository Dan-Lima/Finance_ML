from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import _setit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from math import *

class MachineLearning(object):
	ML_Classification_Alg=("Logistic Regression","Neural Network")
	ML_Regression_Alg=("Multiple Linear Regression","Neural Network")
	ML_Algorithms={"Classification": ML_Classification_Alg, "Regression": ML_Regression_Alg}
	ML_ActivationFunc=("Sigmoid","Relu")

	#Lists to have access the elements
	ModelButtons=[]
	ModelOptionMenus=[]

	def __init__(self):
		#Color palette
		self.window_color="gray10" #background color for toplevel, frames and labels
		self.elements_color="gray25" #background color for elements in buttons and frames
		self.entry_color="gray35" #background color for entries
		self.text_color="gray99" #color of displayed text

		#Creates a new window to define the details of the algorithm to be run
		self.ML_Window = Toplevel()
		self.ML_Window.geometry("400x400")
		self.ML_Window.wm_title("Machine Learning Dashboard")
		self.ML_Window.grab_set()
		self.ML_Window.config(bg=self.window_color)
		self.ML_Window.resizable(False, False)

		#Setting control variables
		self.HasHeader=IntVar()
		self.HasHeader.set(1)

		self.DataImported=False
		self.DataPreview=StringVar()
		self.DeltaCol=1 #the number of columns the display moves each time the user presses the arrow keys
		self.FirstColumnDisplay=0
		self.LastColumnDisplay=5
		self.DeltaRow=1 #the number of rows the display moves each time the user presses the arrow keys
		self.FirstRowDisplay=0
		self.LastRowDisplay=15
		self.ModelType=StringVar()
		self.Algo=StringVar()
		self.ModelType.set(list(MachineLearning.ML_Algorithms.keys())[0])
		self.Algo.set(MachineLearning.ML_Algorithms[self.ModelType.get()][0])

		#Adds main window elements
		self.Frame_ML=Frame(self.ML_Window, bg=self.window_color)
		self.Frame_ML.grid(row=0, column=0, columnspan=2, rowspan=2, padx=5, pady=5)
		
		self.Button_ImportData=Button(self.Frame_ML, text="Import Data", command=self.ImportData, bg=self.elements_color, fg=self.text_color, width=10)
		self.Button_DisplayData=Button(self.Frame_ML, text="Display Data", command=self.DisplayData, bg=self.elements_color, fg=self.text_color, width=10)
		self.Checkbox_Header=Checkbutton(self.Frame_ML, text="Header", variable=self.HasHeader, bg=self.window_color, fg=self.text_color, selectcolor="black")
		
		self.Button_ImportData.grid(row=0, column=0, padx=5, pady=5)
		self.Button_DisplayData.grid(row=1, column=0, padx=5, pady=5)
		self.Checkbox_Header.grid(row=0, column=1, padx=5, pady=5)

		self.Frame_Parameters=Frame(self.ML_Window, bg=self.window_color, borderwidth=2, relief="sunken")
		self.Label_ModelParameters=Label(self.ML_Window, text="Model Parameters", bg=self.window_color, fg=self.text_color)
		self.Label_ModelType=Label(self.Frame_Parameters, text="Type:", bg=self.window_color, fg=self.text_color)
		self.OM_ModelType=OptionMenu(self.Frame_Parameters, self.ModelType, *MachineLearning.ML_Algorithms.keys(), command=self.UpdateAlgos)
		self.OM_ModelType.config(bg=self.elements_color, fg=self.text_color, activebackground=self.elements_color, activeforeground=self.text_color, highlightthickness=0, width=11, anchor=W)
		self.OM_ModelType["menu"].configure(bg=self.elements_color, fg=self.text_color)
		self.Label_Algo=Label(self.Frame_Parameters, text="Algorithm:", bg=self.window_color, fg=self.text_color)
		self.OM_Algo=OptionMenu(self.Frame_Parameters, self.Algo, *MachineLearning.ML_Algorithms[self.ModelType.get()])
		self.OM_Algo.config(bg=self.elements_color, fg=self.text_color, activebackground=self.elements_color, activeforeground=self.text_color, highlightthickness=0, width=22, anchor=W)
		self.OM_Algo["menu"].configure(bg=self.elements_color, fg=self.text_color)

		self.Frame_Parameters.grid(row=4, column=0, columnspan=3, rowspan=2, padx=5, pady=0, sticky=W)
		self.Label_ModelParameters.grid(row=3 , column=0, padx=5, pady=2, sticky=W)
		self.Label_ModelType.grid(row=0, column=0, columnspan=1, rowspan=1, padx=0, pady=5, sticky=W)
		self.OM_ModelType.grid(row=0, column=1, columnspan=2, rowspan=1, padx=5, pady=5, sticky=W)
		self.Label_Algo.grid(row=1, column=0, columnspan=1, rowspan=1, padx=0, pady=5, sticky=W)
		self.OM_Algo.grid(row=1, column=1, columnspan=2, rowspan=1, padx=5, pady=5, sticky=W)

		#1 label for Model Parameters
		#2 frames with sunken borders: one for NN another one for reggressions
		#2 options menus: model type + algorithm
		#function to updates frame (use frame.raise function)

	#Imports the data from a user-specified file
	def ImportData(self):
		File=askopenfilename(initialdir="/", title="Select file", filetypes=(("Excel Workbook", "*.xlsx"), ("Excel 97-2003 Workbook", "*.xls"), ("Comma-separated Values", "*.csv")))

		#Checks the file type provided by the user to pick the appropriate import format
		if self.HasHeader.get():
			if File[-4:]==".xls" or File[-5:]==".xlsx":
				self.Data=pd.read_excel(File)
				messagebox.showinfo("File import", "File successfully imported.")
				self.DataImported = True
				self.Data_Columns=list(self.Data.columns)

			elif File[-4:]==".csv":
				self.Data=pd.read_csv(File)
				messagebox.showinfo("File import", "File successfully imported.")
				self.DataImported = True
				self.Data_Columns=list(self.Data.columns)

			else:
				messagebox.showerror("Invalid file type", "Please import an Excel workbook (.xls or .xlsx) or a .csv file.")
				self.DataImported = False

		else:	
			if File[-4:]==".xls" or File[-5:]==".xlsx":
				self.Data=pd.read_excel(File, header=None)
				messagebox.showinfo("File import", "File successfully imported.")
				self.DataImported = True
				self.Data_Columns=list(self.Data.columns)

			elif File[-4:]==".csv":
				self.Data=pd.read_csv(File, header=None)
				messagebox.showinfo("File import", "File successfully imported.")
				self.DataImported = True
				self.Data_Columns=list(self.Data.columns)

			else:
				messagebox.showerror("Invalid file type", "Please import an Excel workbook (.xls or .xlsx) or a .csv file.")
				self.DataImported = False

	#Show details imported data to the user
	def DisplayData(self):
		#displays a preview of the imported data to the user in a new window
		if self.DataImported:
			self.Window_DisplayData=Toplevel()
			self.Window_DisplayData.geometry("550x280")
			self.Window_DisplayData.wm_title("Imported data")
			self.Window_DisplayData.grab_set()
			self.Window_DisplayData.config(bg=self.window_color)
			self.Window_DisplayData.protocol("WM_DELETE_WINDOW", self.ClosingDisplayData)
			messagebox.showinfo("Data display", "Use the keyboard arrow keys to navigate through the data.\nDouble click to reset the data display.\nPress CTRL+Q to exit.")

			#ajusts string var and adds label to "print" the data to
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.Text_DisplayData=Text(self.Window_DisplayData, bg=self.window_color, fg=self.text_color, borderwidth=0)
			self.Text_DisplayData.grid(row=0, column=0, columnspan=self.DeltaCol, rowspan=self.DeltaRow, padx=5, pady=5)
			self.DisplayUpdateText()
			

			#establishes keyboard binds to navigate through the data
			self.Window_DisplayData.bind('<Double-Button-1>', self.MouseResetDisplay)
			self.Window_DisplayData.bind('<Right>', self.MoveDisplayRight)
			self.Window_DisplayData.bind('<Left>', self.MoveDisplayLeft)
			self.Window_DisplayData.bind('<Down>', self.MoveDisplayDown)
			self.Window_DisplayData.bind('<Up>', self.MoveDisplayUp)
			self.Window_DisplayData.bind('<Control-q>', self.ClosingDisplayData)
			self.Window_DisplayData.bind('<MouseWheel>', self.MouseWheel) #Will only work with Windows

		else:
			messagebox.showerror("No data imported", "You need to import data in order to display it.")

	def ClosingDisplayData(self,event=None):
		self.FirstColumnDisplay=0
		self.LastColumnDisplay=5
		self.FirstRowDisplay=0
		self.LastRowDisplay=15
		self.Window_DisplayData.destroy()
		self.ML_Window.grab_set()

	#The next 6 functions allow the user to check the imported data
	def MouseResetDisplay(self,event=None):
		self.FirstColumnDisplay=0
		self.LastColumnDisplay=5
		self.FirstRowDisplay=0
		self.LastRowDisplay=15
		self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
		self.DisplayUpdateText()

	def MouseWheel(self,event=None):
		if event.num==5 or event.delta==-120:
			self.MoveDisplayDown()
		if event.num==4 or event.delta==120:
			self.MoveDisplayUp()

	def MoveDisplayRight(self,event=None):
		if self.LastColumnDisplay+self.DeltaCol>=self.Data.shape[1]:
			self.LastColumnDisplay=self.Data.shape[1]
			self.FirstColumnDisplay=self.Data.shape[1]-5
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.DisplayUpdateText()

		else:
			self.FirstColumnDisplay+=self.DeltaCol
			self.LastColumnDisplay+=self.DeltaCol
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.DisplayUpdateText()

	def MoveDisplayLeft(self,event=None):
		if self.FirstColumnDisplay-self.DeltaCol<=0:
			self.LastColumnDisplay=5
			self.FirstColumnDisplay=0
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.DisplayUpdateText()

		else:
			self.LastColumnDisplay-=self.DeltaCol
			self.FirstColumnDisplay-=self.DeltaCol
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.DisplayUpdateText()

	def MoveDisplayDown(self,event=None):
		if self.LastRowDisplay+self.DeltaRow>=self.Data.shape[0]:
			self.LastRowDisplay=self.Data.shape[0]
			self.FirstRowDisplay=self.Data.shape[0]-15
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.DisplayUpdateText()

		else:
			self.FirstRowDisplay+=self.DeltaRow
			self.LastRowDisplay+=self.DeltaRow
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.DisplayUpdateText()

	def MoveDisplayUp(self,event=None):
		if self.FirstRowDisplay-self.DeltaRow<=0:
			self.LastRowDisplay=15
			self.FirstRowDisplay=0
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.DisplayUpdateText()

		else:
			self.LastRowDisplay-=self.DeltaRow
			self.FirstRowDisplay-=self.DeltaRow
			self.DataPreview.set(self.Data.iloc[self.FirstRowDisplay:self.LastRowDisplay,self.FirstColumnDisplay:self.LastColumnDisplay].to_string())
			self.DisplayUpdateText()

	#updates the data displayed under the Display Data button
	def DisplayUpdateText(self):
		self.Text_DisplayData.configure(state='normal')
		self.Text_DisplayData.delete('1.0', END)
		self.Text_DisplayData.insert('1.0', self.DataPreview.get())
		self.Text_DisplayData.configure(state='disabled')
	
	#Updates Algo OptionMenu given the Model Type selected by the user:
	def UpdateAlgos(self,event):
		self.Algo.set(MachineLearning.ML_Algorithms[self.ModelType.get()][0])
		self.OM_Algo['menu'].delete(0,'end')

		for option in list(MachineLearning.ML_Algorithms[self.ModelType.get()]):
			self.OM_Algo['menu'].add_command(label=option, command=_setit(self.Algo, option))

	#Creates menu for model parameters after the data has been imported
	def ModelParameters(self):
		pass

	#Cleans the data, removes empty values, etc
	def CleanData(self):
		pass

	#Validates the data provided
	def ValidateData(self):
		pass

	#Prepares the data for the modelling phase
	def PrepareData(self):
		pass

	#Organizes the modelling phase according user's inputs
	def ModelData(self):
		pass

	def Sigmoid(self):
		pass

	def Relu(self):
		pass

	def DSigmoid(self):
		pass

	def DRelu(self):
		pass

	def MLR(self):
		pass

	def LogisticRegError(self):
		pass

	def GradientDescent(self, Learning_Rate):
		pass

	def ForwardPropagation(self):
		pass

	def BackPropagation(self):
		pass

	#Memory management
	# def __del__(self):
	# 	pass