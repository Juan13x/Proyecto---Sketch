import tkinter as tk
from tkinter import scrolledtext
import tkinter.font  as tkFont
from PIL import ImageTk, Image
from constants_AND_variables import *
from Interface_Functions import *

mainWindow = tk.Tk()

mainWindow.geometry(sizes['window'])
mainWindow.title(strings['windowTitle'])

RadioButtonVertices = tk.IntVar()
RadioButtonOperation =  tk.IntVar()
RadioButtonTypeSelection = tk.IntVar()

def initRadioButtons():
    RadioButtonVertices.set(strings['clickVertices']['optionVerticesManual'])
    RadioButtonTypeSelection.set(strings['clickTypeSelection']['optionTypeSelectionImage'])
    RadioButtonOperation.set(strings['clickOperation']['optionOperationOneByOne'])

initRadioButtons()

#INFO PHOTO1
widget_infoPhoto1 = tk.Label(mainWindow, text = strings['infoPhoto1'], bd=1, relief=tk.SOLID)
widget_infoPhoto1.place(
    x = pos['infoPhoto1'][0],
    y = pos['infoPhoto1'][1],
    width = sizes['infoPhoto1'][0],
    height = sizes['infoPhoto1'][1])

#PHOTO1
sourceImage = Image.open(images['photo1'])
sourceImage = sourceImage.resize(sizes['photo1'])
imagePhoto1 = ImageTk.PhotoImage(sourceImage)
widget_photo1 = tk.Label(mainWindow, image = imagePhoto1)
widget_photo1.place(
    x = pos['photo1'][0], 
    y = pos['photo1'][1])

#INFO PHOTO2
widget_infoPhoto2 = tk.Label(mainWindow, text = strings['infoPhoto2'], bd=1, relief=tk.SOLID)
widget_infoPhoto2.place(
    x = pos['infoPhoto2'][0],
    y = pos['infoPhoto2'][1],
    width = sizes['infoPhoto2'][0],
    height = sizes['infoPhoto2'][1])

#PHOTO2
sourceImage = Image.open(images['photo2'])
sourceImage = sourceImage.resize(sizes['photo2'])
imagePhoto2 = ImageTk.PhotoImage(sourceImage)
widget_photo2 = tk.Label(mainWindow, image=imagePhoto2)
widget_photo2.place(
    x = pos['photo2'][0], 
    y = pos['photo2'][1])

#LOGO
sourceImage = Image.open(images['LOGO']) 
sourceImage = sourceImage.resize(sizes['LOGO'])
imageLogo = ImageTk.PhotoImage(sourceImage)
widget_logo = tk.Label(mainWindow, image = imageLogo)
widget_logo.place(
    x = pos['LOGO'][0], 
    y = pos['LOGO'][1])

#SELECTED
sourceImage = Image.open(images['selected'])
sourceImage = sourceImage.resize(sizes['selected'])
defaultSelectedImage = ImageTk.PhotoImage(sourceImage)
widget_selectedImage = tk.Label(mainWindow, image = defaultSelectedImage, bd=1, relief=tk.SOLID)
widget_selectedImage.place(
    x = pos['selected'][0], 
    y = pos['selected'][1],
    width = sizes['selected'][0], 
    height = sizes['selected'][1])

#BUTTON BACK
widget_buttonBack = tk.Button(mainWindow, text = strings['buttonBack'])
widget_buttonBack['state'] = "disable"
widget_buttonBack.place(
    x = pos['buttonBack'][0],
    y = pos['buttonBack'][1],
    width = sizes['buttonBack'][0],
    height = sizes['buttonBack'][1])

#BUTTON NEXT
widget_buttonNext = tk.Button(mainWindow, text = strings['buttonNext'])
widget_buttonNext['state'] = "disable"
widget_buttonNext.place(
    x = pos['buttonNext'][0],
    y = pos['buttonNext'][1],
    width = sizes['buttonNext'][0],
    height = sizes['buttonNext'][1])

#UPDATE
#BUTTON SUBMIT
widget_update = tk.Button(mainWindow, text = strings['update'])
widget_update.place(
    x = pos['update'][0],
    y = pos['update'][1],
    width = sizes['update'][0],
    height = sizes['update'][1])

#RESULT
widget_result = tk.Text(mainWindow, bd=1, relief=tk.SOLID)
widget_result.place(
    x = pos['result'][0],
    y = pos['result'][1],
    width = sizes['result'][0],
    height = sizes['result'][1])

#BUTTON RESET
widget_reset = tk.Button(mainWindow, text = strings['reset'])
widget_reset.place(
    x = pos['reset'][0],
    y = pos['reset'][1],
    width = sizes['reset'][0],
    height = sizes['reset'][1])

#BUTTON SAVE
widget_save = tk.Button(mainWindow, text = strings['save'])
widget_save.place(
    x = pos['save'][0],
    y = pos['save'][1],
    width = sizes['save'][0],
    height = sizes['save'][1])

#BUTTON SUBMIT
widget_submit = tk.Button(mainWindow, text = strings['submit'])
widget_submit['state'] = "disable"
widget_submit.place(
    x = pos['submit'][0],
    y = pos['submit'][1],
    width = sizes['submit'][0],
    height = sizes['submit'][1])

#FOLDER CHOICE
sourceImage = Image.open(images["folderChoice"])
sourceImage = sourceImage.resize(sizes['folderChoice'])
folderChoiceIcon = ImageTk.PhotoImage(sourceImage)
widget_folderChoice = tk.Button(mainWindow, image=folderChoiceIcon)
widget_folderChoice.place(
    x = pos['folderChoice'][0],
    y = pos['folderChoice'][1])

#FOLDER DIRECTION
widget_folderDirection = tk.Label(mainWindow, text="", bg = "#FFFFFF", anchor=tk.E)
widget_folderDirection.place(
    x = pos["folderDirection"][0],
    y = pos["folderDirection"][1],
    width = sizes["folderDirection"][0],
    height = sizes["folderDirection"][1]
    )

#INFO SELECTION
widget_infoSelection = tk.Label(mainWindow, text = strings['infoSelection'], bd = 1, relief=tk.GROOVE)
widget_infoSelection.place(
    x = pos["infoSelection"][0],
    y = pos["infoSelection"][1],
    width = sizes["infoSelection"][0],
    height = sizes["infoSelection"][1])

#SELECTION ITEM 1
widget_optionTypeSelectionDiretory = tk.Radiobutton(mainWindow, text = strings['optionTypeSelectionDiretory'], variable = RadioButtonTypeSelection, value = strings['clickTypeSelection']['optionTypeSelectionDirectory'])
widget_optionTypeSelectionDiretory.place(
    x = pos['optionTypeSelectionDiretory'][0], 
    y = pos['optionTypeSelectionDiretory'][1],
    width = sizes['optionTypeSelection'][0],
    height = sizes['optionTypeSelection'][1])

#SELECTION ITEM 2
widget_optionTypeSelectionImage = tk.Radiobutton(mainWindow, text = strings['optionTypeSelectionImage'], variable = RadioButtonTypeSelection, value = strings['clickTypeSelection']['optionTypeSelectionImage'], state = 'disabled')
widget_optionTypeSelectionImage.place(
    x = pos['optionTypeSelectionImage'][0], 
    y = pos['optionTypeSelectionImage'][1],
    width = sizes['optionTypeSelection'][0],
    height = sizes['optionTypeSelection'][1])

#INFO OPERATION
widget_infoOperation = tk.Label(mainWindow, text = strings['infoOperation'], bd = 1, relief=tk.GROOVE)
widget_infoOperation.place(
    x = pos["infoOperation"][0],
    y = pos["infoOperation"][1],
    width = sizes["infoOperation"][0],
    height = sizes["infoOperation"][1])

#OPERATION ITEM 1
widget_optionOperationOneByOne = tk.Radiobutton(mainWindow, text = strings['optionOperationOneByOne'], variable = RadioButtonOperation, value = strings['clickOperation']['optionOperationOneByOne'], state = 'disabled')
widget_optionOperationOneByOne.place(
    x = pos['optionOperationOneByOne'][0], 
    y = pos['optionOperationOneByOne'][1],
    width = sizes['optionOperation'][0],
    height = sizes['optionOperation'][1])

#OPERATION ITEM 2
widget_optionOperationAll = tk.Radiobutton(mainWindow, text = strings['optionOperationAll'], variable = RadioButtonOperation, value = strings['clickOperation']['optionOperationAll'])
widget_optionOperationAll.place(
    x = pos['optionOperationAll'][0], 
    y = pos['optionOperationAll'][1],
    width = sizes['optionOperation'][0],
    height = sizes['optionOperation'][1])

#INFO VERTICES
widget_infoOperation = tk.Label(mainWindow, text = strings['infoVertices'], bd = 1, relief=tk.GROOVE)
widget_infoOperation.place(
    x = pos["infoVertices"][0],
    y = pos["infoVertices"][1],
    width = sizes["infoVertices"][0],
    height = sizes["infoVertices"][1])

#VERTICES MODE ITEM 1
widget_optionVerticesManual = tk.Radiobutton(mainWindow, text = strings['optionVerticesManual'], variable = RadioButtonVertices, value = strings['clickVertices']['optionVerticesManual'], state = 'disabled')
widget_optionVerticesManual.place(
    x = pos["optionVerticesManual"][0],
    y = pos["optionVerticesManual"][1],
    width = sizes["optionVertices"][0],
    height = sizes["optionVertices"][1])


#VERTICES MODE ITEM 2
widget_optionVerticesAuto = tk.Radiobutton(mainWindow, text = strings['optionVerticesAuto'], variable = RadioButtonVertices, value = strings['clickVertices']['optionVerticesAuto'])
widget_optionVerticesAuto.place(
    x = pos["optionVerticesAuto"][0],
    y = pos["optionVerticesAuto"][1],
    width = sizes["optionVertices"][0],
    height = sizes["optionVertices"][1])

#TITLE
fontExample = tkFont.Font(family="Arial", size=18, weight="bold", slant="italic")
title = tk.Label(mainWindow, text=strings['title'], bd=1, relief=tk.SUNKEN, font=fontExample)
title.place(
    x = pos['title'][0], 
    y = pos['title'][1],
    width = sizes['title'][0],
    height = sizes['title'][1])
