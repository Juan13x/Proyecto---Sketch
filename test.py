from interface import *
from Interface_Functions import *

widget_folderChoice.configure(command=clickFolderChoice)
widget_optionTypeSelectionDiretory.configure(command = clickTypeSelection)
widget_optionTypeSelectionImage.configure(command = clickTypeSelection)
widget_update.configure(command=clickUpdate)
widget_optionVerticesManual.configure(command = clickVertices)
widget_optionVerticesAuto.configure(command = clickVertices)
widget_optionOperationAll.configure(command = clickOperation)
widget_optionOperationOneByOne.configure(command = clickOperation)
widget_save.configure(command = clickSave)
widget_reset.configure(command = clickReset)
widget_submit.configure(command = clickSubmit)

tk.mainloop()
mainWindow.destroy()

'''
DATA:
-look for data set: NOT READY

prepocesado:
-tomar imagen : READY
-obtener vertices : READY
-Organizar perspectiva manual: READY
-Organizar perspectiva automática: READY
-posiblemente, GRAY : READY
-Mejorar el constraste : READY
-Binarizar: del gray o del espacio de color: Semi - READY

PRIMERA VERSION:
################################
Básica:
-OCR:
    -tesseract: READY
    -easyOCR: NOT READY?

caso1:
OCR:
    -Machine Learning:
        -set fonts: Carácteres
            -Formato: en
                -clasificar
                -set de caracteristicas

caso2:
OCR:
    -Deep Learning:
        -set fonts: Carácteres
            -Formato: en
                -red neuronal

caso3:
    -Relación centro imagen-Alrededor

RESULTADO:
-EditText: por si se quiere cambiar

SEGUNDA VERSION
################################
-Pasar el edit text a un docx, txt, etc.

TERCERA VERSION: solo por joder
################################
-CONSECUTIVE MASS SCANNING

Anotaciones:
-primero: solo textos en inglés

MEDIO DE TRABABJO:
-entorno virtual: 3.8.10
-live share

INTERFAZ:
PRIMERA VERSION:
################################
-Una imagen a la izquierda (foto original)
-One Image to the rightest for the proceess
-En la mitad un botón de opciones: Manual o Automática para vertices
-Conversion button

SEGUNDA VERSION
################################
-Save button

TERCERA VERSION: solo por joder
################################
-Opción (switch): Concatenar o único

Propuestas:
1: hacer interfaz
2: hacer preprocesado
3: hacer OCR (sección 'básica')
4: Los 2 buscar sobre ML
5: Los 2 buscar sobre DL
'''