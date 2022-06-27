import interface as itk
from PIL import ImageTk, Image
from constants_AND_variables import *
from functions import *
from tkinter import filedialog

def clickTypeSelection():
    if(itk.RadioButtonTypeSelection.get() == strings['clickTypeSelection']['optionTypeSelectionDirectory']):
        itk.widget_optionTypeSelectionDiretory.configure(state = "disable")
        itk.widget_optionTypeSelectionImage.configure(state = "active")
    else:
        itk.widget_optionTypeSelectionImage.configure(state = "disable")
        itk.widget_optionTypeSelectionDiretory.configure(state = "active")

def clickFolderChoice():
    if(itk.RadioButtonTypeSelection.get() == strings['clickTypeSelection']['optionTypeSelectionDirectory']):
        filedir = filedialog.askdirectory(initialdir = strings['clickFolderChoice']['optionTypeSelectionDirectory']['initialdir'], title = strings['clickFolderChoice']['optionTypeSelectionDirectory']['title'], mustexist = True)
        itk.widget_folderDirection.configure(text = filedir)
    else:
        filename = filedialog.askopenfilename(initialdir=strings['clickFolderChoice']['optionTypeSelectionImage']['initialdir'], title = strings['clickFolderChoice']['optionTypeSelectionImage']['title'], filetypes = strings['clickFolderChoice']['optionTypeSelectionImage']['filetypes'])
        itk.widget_folderDirection.configure(text = filename)

def clickUpdate():
    path = str(itk.widget_folderDirection.cget('text'))

    if(path!=""):
        if(itk.RadioButtonTypeSelection.get() == strings['clickTypeSelection']['optionTypeSelectionDirectory']):
            OkToprocess = True
            #TODO: verify there are images in the folder. OkToprocess
            if(OkToprocess):
                itk.widget_buttonBack.configure(state = "active")
                itk.widget_buttonNext.configure(state = "active")
                strings['clickFolderChoice']['optionTypeSelectionDirectory']['initialdir'] = path
            OkToprocess = False
        else:
            OkToprocess = True
            itk.widget_buttonBack.configure(state = "disable")
            itk.widget_buttonNext.configure(state = "disable")
            strings['clickFolderChoice']['optionTypeSelectionImage']['initialdir'] = getDirectoryFromImagePath(path)
            setImageSelected(path)

        if(OkToprocess):
            drawSelectedImage(getImageSelected())
            itk.widget_submit.configure(state = "active")
            
        else:
            itk.widget_submit.configure(state = "disable")
            itk.widget_selectedImage.configure(image="")

def clickOperation():
    if(itk.RadioButtonOperation.get() == strings['clickOperation']['optionOperationOneByOne']):
        itk.widget_optionOperationOneByOne.configure(state = 'disable')
        itk.widget_optionOperationAll.configure(state = 'active')
    else:
        itk.widget_optionOperationOneByOne.configure(state = 'active')
        itk.widget_optionOperationAll.configure(state = 'disable')

def clickVertices():
    if(itk.RadioButtonVertices.get() == strings['clickVertices']['optionVerticesManual']):
        itk.widget_optionVerticesManual.configure(state = 'disable')
        itk.widget_optionVerticesAuto.configure(state = 'active')
    else:
        itk.widget_optionVerticesManual.configure(state = 'active')
        itk.widget_optionVerticesAuto.configure(state = 'disable')

def clickReset():
    setResult("")
    itk.widget_result.delete(1.0, "end")

def clickSave():
    with open("savedText.txt", "w", encoding = 'utf-8') as f:
        for c in getResult():
            f.write(c)

def clickSubmit():
    PDI_process()

def drawSelectedImage(path:str):
    global sourceImage
    sourceImage = Image.open(path)
    sourceImage = sourceImage.resize(sizes['selected'])
    sourceImage = ImageTk.PhotoImage(sourceImage)
    itk.widget_selectedImage.grid_forget()
    itk.widget_selectedImage.configure(image = sourceImage)