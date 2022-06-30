import cv2
import numpy as np
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def histEcu(img,alpha,grid):
    if alpha!=0:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        L,A,B=cv2.split(img)
        clahe = cv2.createCLAHE(clipLimit=alpha, tileGridSize=grid)
        cl = clahe.apply(L)
        img = cv2.merge((cl,A,B))
        img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
    return img

def ordenar_puntos(puntos):
	n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()

	y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])

	x1_order = y_order[:2]
	x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])

	x2_order = y_order[2:4]
	x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
	
	return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

image = cv2.imread("./default_Selection_dir/img_00.jpeg")

alpha=5 #Parametro a ser cambiado más adelante por el usuario en interfaz
grid=(10,10) #PArametro que puede ser cambiado más adelante con interfaz
image=histEcu(image,alpha,grid)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,bin = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
canny = cv2.Canny(bin, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)

cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]
dst = 0

for c in cnts:
    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    
    if len(approx)==4:
        cv2.drawContours(image, [approx], 0, (0,255,255),2)
        
        puntos = ordenar_puntos(approx)

        cv2.circle(image, tuple(puntos[0]), 7, (255,0,0), 2)
        cv2.circle(image, tuple(puntos[1]), 7, (0,255,0), 2)
        cv2.circle(image, tuple(puntos[2]), 7, (0,0,255), 2)
        cv2.circle(image, tuple(puntos[3]), 7, (255,255,0), 2)
        
        pts1 = np.float32(puntos)
        pts2 = np.float32([[0,0],[270,0],[0,310],[270,310]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(gray,M,(270,310))
        break
cv2.waitKey(0)

# NOTE: all row, words and characters are save in a list: outer most elements are rows, middle-depth elements are words and inner most ones are chars

# TODO: Enhance contrast: Contrast Adjust, Equaliziton, etc... (In process)
# TODO: Binarize (done)
# TODO: Separate rows by using histogram or other technique
# TODO: Separate words  of each row by using histogram or other technique
# TODO: Seperate each word from each words
# TODO: apply pytesseract or EASYOCR to check effectiveness at recovering the character
# TODO: apply Machine Learning (in process)
# TODO: apply Deep Learning

# texto = pytesseract.image_to_string(dst, lang='spa')
# print(texto)

# cv2.imshow('Result', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()