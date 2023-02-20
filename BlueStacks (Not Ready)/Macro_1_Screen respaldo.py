import cv2
import numpy as np
import pyautogui
import time

start_time = time.time()
Minirana = [
  '0_0.png',  '0_1.png',  '0_2.png',  '0_3.png',  '0_4.png',
  '0_5.png',  '0_6.png',  '0_7.png',  '0_8.png',  '0_9.png',
  '0_10.png', '0_11.png', '0_12.png', '0_13.png', '0_14.png',
  '0_15.png', '0_16.png', '0_17.png', '0_18.png', '0_19.png',
  '0_20.png'
    
]
Darkcloud = [
  '1_0.png',  '1_1.png',  '1_2.png',  '1_3.png',  '1_4.png',
  '1_5.png',  '1_6.png',  '1_7.png',  '1_8.png',  '1_9.png',
  '1_10.png', '1_11.png', '1_12.png', '1_13.png', '1_14.png',
  '1_15.png', '1_16.png', '1_17.png', '1_18.png', '1_19.png',
  '1_20.png'
    
]
Diego1000 = [
  '2_0.png',  '2_1.png',  '2_2.png',  '2_3.png',  '2_4.png',
  '2_5.png',  '2_6.png',  '2_7.png',  '2_8.png',  '2_9.png',
  '2_10.png', '2_11.png', '2_12.png', '2_13.png', '2_14.png',
  '2_15.png', '2_16.png', '2_17.png', '2_18.png', '2_19.png',
  '2_20.png'
]
Diego1001 = [
  '3_0.png',  '3_1.png',  '3_2.png',  '3_3.png',  '3_4.png',
  '3_5.png',  '3_6.png',  '3_7.png',  '3_8.png',  '3_9.png',
  '3_10.png', '3_11.png', '3_12.png', '3_13.png', '3_14.png',
  '3_15.png', '3_16.png', '3_17.png', '3_18.png', '3_19.png',
  '3_20.png'
]
Diego1002 = [
  '4_0.png',  '4_1.png',  '4_2.png',  '4_3.png',  '4_4.png',
  '4_5.png',  '4_6.png',  '4_7.png',  '4_8.png',  '4_9.png',
  '4_10.png', '4_11.png', '4_12.png', '4_13.png', '4_14.png',
  '4_15.png', '4_16.png', '4_17.png', '4_18.png', '4_19.png',
  '4_20.png'
]

def encontrar_plantilla(imagen, plantilla):
    img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    plantilla_img = cv2.imread(plantilla, 0)
    res = cv2.matchTemplate(img_gris, plantilla_img, cv2.TM_CCOEFF_NORMED)
    min_valS1, max_valS1, min_locS1, max_locS1 = cv2.minMaxLoc(res)
    
    max_value.append(max_valS1)
    umbral = 0.8
    loc = np.where(res >= umbral)
    
    return max_value


imagen =  pyautogui.screenshot()
imagen = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", imagen)
imagen = cv2.imread('in_memory_to_disk.png')

max_value = []

for plantilla in Minirana:
    max_value_minirana = encontrar_plantilla(imagen, plantilla)
    max_value_minirana = max(max_value_minirana)
for plantilla in Darkcloud:
    max_value_darkcloud = encontrar_plantilla(imagen, plantilla)
    max_value_darkcloud = max(max_value_darkcloud)

    
end_time = time.time()
elapsed_time = end_time - start_time
print('Este es el valor maximo encontrado en el array de Minirana:', max_value_minirana)
print('Este es el valor maximo encontrado en el array de Darkcloud:', max_value_darkcloud)
#print('Este es el valor maximo encontrado en el array de Diego1000:', max_value_diego1000)
#print('Este es el valor maximo encontrado en el array de Diego1001:', max_value_diego1001)
#print('Este es el valor maximo encontrado en el array de Diego1002:', max_value_diego1002)
#print(f"Elapsed time: {elapsed_time:.2f} seconds")

