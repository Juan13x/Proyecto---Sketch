import cv2
import interface as itk
from constants_AND_variables import *


def getDirectoryFromImagePath(varSTR : str)-> str:   
    index : int
    #move along the string from end to start
    for c in range(len(varSTR)-1, -1, -1): 
        if(varSTR[c] == "\\" or varSTR[c] == "/"):
            index = c
            break
    return varSTR[:index]


def PDI_process():
    if(getCounterTest() == len(test)):
        resetCounterTest()
    
    setResult(getResult() + test[getCounterTest()])
    itk.widget_result.delete(1.0, "end")
    itk.widget_result.insert(1.0, getResult())
    incrementCounterTest()