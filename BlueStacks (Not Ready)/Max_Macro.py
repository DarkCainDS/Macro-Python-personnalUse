import cv2 as cv
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
    max_value = []
    max_value.append(max_valS1)
    return max_value
imagen =  pyautogui.screenshot()
imagen = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", imagen)
imagen = cv2.imread('in_memory_to_disk.png')


for plantilla in Minirana:
    max_value_minirana = encontrar_plantilla(imagen, plantilla)

for plantilla in Darkcloud:
    max_value_darkcloud = encontrar_plantilla(imagen, plantilla)

for plantilla in Diego1000:
    max_value_diego1000 = encontrar_plantilla(imagen, plantilla)
for plantilla in Diego1001:
    max_value_diego1001 = encontrar_plantilla(imagen, plantilla)
for plantilla in Diego1002:
    max_value_diego1002 = encontrar_plantilla(imagen, plantilla)
    
end_time = time.time()
elapsed_time = end_time - start_time


    
def clicker(S1,S2,S3,S4,S5):
    if S1 == 1:
        pyautogui.click(x=1900, y=595)
        time.sleep(1)
        pyautogui.click(x=1780, y=466)
        
    elif S2 == 1:
        pyautogui.click(x=1900, y=932)
        time.sleep(1)
        pyautogui.click(x=1780, y=800)
    elif S3 == 1:
        pyautogui.click(x=775, y=955)
        time.sleep(1)
        pyautogui.click(x=635, y=685)
    elif S4 == 1:
        pyautogui.click(x=773, y=441)
        time.sleep(1)
        pyautogui.click(x=630, y=160)
        time.sleep(1)
    elif S5 == 1:
        pyautogui.click(x=1900, y=255)
        time.sleep(1)
        pyautogui.click(x=1780, y=122)

        
    #Find Opponent
    
    pyautogui.click(x=370, y=424)
    pyautogui.click(x=370, y=935)
    pyautogui.click(x=1570, y=275)
    pyautogui.click(x=1570, y=612)
    pyautogui.click(x=1570, y=946)
    time.sleep(3)
    #Fight!
    pyautogui.click(x=530, y=350)
    pyautogui.click(x=530, y=865)
    pyautogui.click(x=1700, y=230)
    pyautogui.click(x=1700, y=565)
    pyautogui.click(x=1700, y=900)
    time.sleep(4.5)
    #Collect
    pyautogui.click(x=370, y=456)
    pyautogui.click(x=370, y=968)
    pyautogui.click(x=1560, y=294)
    pyautogui.click(x=1560, y=635)
    pyautogui.click(x=1560, y=966)
    

for i in range(300):


    if max_value_minirana >= threshold:
        print('found match MR')
        S1 = 0
    else:
        print('not found match MR')
        S1 = 1
    if max_value_darkcloud >= threshold:
        print('found match DC')
        S2 = 0
    else:
        print('not found match DC')
        S2 = 1

    if max_value_diego1000 >= threshold:
        print('found match D00')
        S3 = 0

    else:
        print('not found match D00')
        S3 = 1

    if max_value_diego1001 >= threshold:
        print('found match D01')
        S4 = 0

    else:
        print('not found match D01')
        S4 = 1

    if max_value_diego1002 >= threshold:
        print('found match D02')
        S5 = 0

    else:
        print('not found match D02')
        S5 = 1
    clicker(S1,S2,S3,S4,S5)
    
    desktop =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
    desktop = cv.cvtColor(np.array(desktop), cv.COLOR_RGB2BGR)


    cv.imwrite("in_memory_to_disk.png", desktop)

    resultS1 = cv.matchTemplate(desktop, minirana, cv.TM_CCOEFF_NORMED)
    resultS2 = cv.matchTemplate(desktop, darkcloud, cv.TM_CCOEFF_NORMED)
    resultS3 = cv.matchTemplate(desktop, diego1000, cv.TM_CCOEFF_NORMED)
    resultS4 = cv.matchTemplate(desktop, diego1001, cv.TM_CCOEFF_NORMED)
    resultS5 = cv.matchTemplate(desktop, diego1002, cv.TM_CCOEFF_NORMED)

    min_valS1, max_valS1, min_locS1, max_locS1 = cv.minMaxLoc(resultS1)
    min_valS2, max_valS2, min_locS2, max_locS2 = cv.minMaxLoc(resultS2)
    min_valS3, max_valS3, min_locS3, max_locS3 = cv.minMaxLoc(resultS3)
    min_valS4, max_valS4, min_locS4, max_locS4 = cv.minMaxLoc(resultS4)
    min_valS5, max_valS5, min_locS5, max_locS5 = cv.minMaxLoc(resultS5)

