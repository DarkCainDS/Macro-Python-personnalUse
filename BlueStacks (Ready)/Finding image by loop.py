import cv2
import numpy as np
import pyautogui
Diego1000 = [
  '0_0.png',  '0_1.png',  '0_2.png',  '0_3.png',  '0_4.png',
  '0_5.png',  '0_6.png',  '0_7.png',  '0_8.png',  '0_9.png',
  '0_10.png', '0_11.png', '0_12.png', '0_13.png', '0_14.png',
  '0_15.png', '0_16.png', '0_17.png', '0_18.png', '0_19.png'
]

def encontrar_plantilla(imagen, plantilla):
    img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    plantilla_img = cv2.imread(plantilla, 0)
    res = cv2.matchTemplate(img_gris, plantilla_img, cv2.TM_CCOEFF_NORMED)
    min_valS1, max_valS1, min_locS1, max_locS1 = cv2.minMaxLoc(res)
    max_value.append(max_valS1)
    umbral = 0.8
    loc = np.where(res >= umbral)
    return loc


imagen =  pyautogui.screenshot()
imagen = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", imagen)
imagen = cv2.imread('in_memory_to_disk.png')

max_value = []
for plantilla in Diego1000:
    loc = encontrar_plantilla(imagen, plantilla)

max_value = max(max_value)
print('Este es el valor maximo encontrado en el array', max_value)

