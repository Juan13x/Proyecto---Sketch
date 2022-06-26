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

PROCESO SKETCH:
variables:
directory_image
image_container
image_counter
image_selected
result

proceso:
-directory click: 
    -setea variable directory_image
    -disable itself
    -disable next and back
-One image click: 
    -Reset variable directory_image
    -disable itself
    -disable next and back

-click carpeta:
    -abre una ventana con opciones según la directory_image

-click update:
    -enable next and back if is_set(directory_image)
    -resetea image_counter
    -actualiza image_container depending on directory_image
    -runs "selectImage"

click back or next:
    -increment or decrement counter_image
    -changes image_selected

click submit:
    -calls OCR_process()
    -sets widget_result

clickreset:
    -reset result
    -sets widget_result

click save:
    -saves result as an .txt
    -sets widget_result with "file saved".

functions:
Get_images_directory():
    -create list of names of images from the directory
selectImage(): 
    -assigns image_selected from image_counter
    -modify image_counter (if directory_image)
OCR_process():
    -OCR process...
'''