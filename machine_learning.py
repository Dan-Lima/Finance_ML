from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
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
	AllFrames=[]
	AllLabels=[]

	def __init__(self):
		#Color palette
		self.window_color="gray10" #background color for toplevel, frames and labels
		self.elements_color="gray25" #background color for elements in buttons and frames
		self.entry_color="gray35" #background color for entries
		self.text_color="gray70" #color of displayed text

		#Creates a new window to define the details of the algorithm to be run
		self.ML_Window = Toplevel()
		self.ML_Window.geometry("400x400")
		self.ML_Window.wm_title("Machine Learning Dashboard")
		self.ML_Window.grab_set()
		self.ML_Window.config(bg=self.window_color)
		#self.ML_Window.resizable(False, False)

		#Setting control variables
		self.DataImported=False

		#Adds main window elements
		Frame_ML=Frame(self.ML_Window, bg=self.window_color, relief=SUNKEN)
		Frame_ML.grid(row=0, column=0, padx=5, pady=5)
		
		Button_ImportData=Button(Frame_ML, text="Import Data", command= self.ImportData, bg=self.elements_color, fg=self.text_color)
		self.HasHeader=IntVar()
		Checkbox_Header=Checkbutton(Frame_ML, text="Header", variable=self.HasHeader, bg=self.window_color, fg=self.text_color)
		
		Button_ImportData.grid(row=0, column=0, padx=5, pady=5)
		Checkbox_Header.grid(row=0, column=1, padx=5, pady=5)

	#Imports the data from a user-specified file
	def ImportData(self):
		File=askopenfilename(initialdir="/", title="Select file", filetypes=(("Excel Workbook", "*.xlsx"), ("Excel 97-2003 Workbook", "*.xls"), ("Comma-separated Values", "*.csv")))

		#Checks the file type provided by the user to pick the appropriate import format
		if self.HasHeader.get():
			if File[-4:]==".xls" or File[-5:]==".xlsx":
				self.Data=pd.read_excel(File)
				messagebox.showinfo("File import", "File successfully imported.")
				self.DataImported = True

			elif File[-4:]==".csv":
				self.Data=pd.read_csv(File)
				messagebox.showinfo("File import", "File successfully imported.")
				self.DataImported = True

			else:
				messagebox.showerror("Invalid file type", "Please import an Excel workbook (.xls or .xlsx) or a .csv file.")
				self.DataImported = False

		else:	
			if File[-4:]==".xls" or File[-5:]==".xlsx":
				self.Data=pd.read_excel(File, header=None)
				messagebox.showinfo("File import", "File successfully imported.")
				self.DataImported = True

			elif File[-4:]==".csv":
				self.Data=pd.read_csv(File, header=None)
				messagebox.showinfo("File import", "File successfully imported.")
				self.DataImported = True

			else:
				messagebox.showerror("Invalid file type", "Please import an Excel workbook (.xls or .xlsx) or a .csv file.")
				self.DataImported = False

		self.DisplayData()

	#Show details imported data to the user
	def DisplayData(self):
		if self.DataImported:
			Frame_DisplayData=Frame(self.ML_Window, bg=self.window_color, relief=SUNKEN)
			Label_DisplayData=Label(Frame_DisplayData, text=self.Data.head().to_string(), bg=self.window_color, fg=self.text_color, bd=2)
			
			Frame_DisplayData.grid(row=1, column=0, padx=5, pady=5)
			Label_DisplayData.grid(row=0, column=0, padx=5, pady=5)
			
			self.Data_Columns=list(self.Data.columns)

			MachineLearning.AllFrames.append(Frame_DisplayData)
			MachineLearning.AllLabels.append(Label_DisplayData)


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