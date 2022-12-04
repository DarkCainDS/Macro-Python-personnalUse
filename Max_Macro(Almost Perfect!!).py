import cv2 as cv
import numpy as np
import pyautogui
import time

minirana = cv.imread('minirana_2.png', cv.IMREAD_UNCHANGED)
darkcloud = cv.imread('darkcloud_2.png', cv.IMREAD_UNCHANGED)
diego1000 = cv.imread('diego1000_2.png', cv.IMREAD_UNCHANGED)
diego1001 = cv.imread('diego1001_2.png', cv.IMREAD_UNCHANGED)
diego1002 = cv.imread('diego1002_2.png', cv.IMREAD_UNCHANGED)

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

threshold = 0.8


    
def clicker(S1,S2,S3,S4,S5):
    if S1 == 1:
        pyautogui.click(x=1900, y=618)
        time.sleep(1)
        pyautogui.click(x=1780, y=476)
    elif S2 == 1:
        pyautogui.click(x=1895, y=965)
        time.sleep(1)
        pyautogui.click(x=1774, y=817)
    elif S3 == 1:
        pyautogui.click(x=827, y=894)
        time.sleep(1)
        pyautogui.click(x=680, y=640)
    elif S4 == 1:
        pyautogui.click(x=826, y=405)
        time.sleep(1)
        pyautogui.click(x=680, y=147)
    elif S5 == 1:
        pyautogui.click(x=1896, y=277)
        time.sleep(1)
        pyautogui.click(x=1770, y=127)

        
    #Find Opponent
    pyautogui.click(x=390, y=400)
    pyautogui.click(x=390, y=887)
    pyautogui.click(x=1570, y=284)
    pyautogui.click(x=1570, y=636)
    pyautogui.click(x=1570, y=975)
    time.sleep(3)
    #Fight!
    pyautogui.click(x=608, y=326)
    pyautogui.click(x=608, y=818)
    pyautogui.click(x=1700, y=234)
    pyautogui.click(x=1700, y=588)
    pyautogui.click(x=1700, y=920)
    time.sleep(4.5)
    #Collect
    pyautogui.click(x=400, y=425)
    pyautogui.click(x=400, y=910)
    pyautogui.click(x=1560, y=308)
    pyautogui.click(x=1560, y=657)
    pyautogui.click(x=1560, y=998)
    

for i in range(300):

    minirana = cv.imread('minirana_2.png', cv.IMREAD_UNCHANGED)
    darkcloud = cv.imread('darkcloud_2.png', cv.IMREAD_UNCHANGED)
    diego1000 = cv.imread('diego1000_2.png', cv.IMREAD_UNCHANGED)
    diego1001 = cv.imread('diego1001_2.png', cv.IMREAD_UNCHANGED)
    diego1002 = cv.imread('diego1002_2.png', cv.IMREAD_UNCHANGED)

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

    threshold = 0.8




    if max_valS1 >= threshold:
        print('found match MR')
        S1 = 0
    else:
        print('not found match MR')
        S1 = 1
    if max_valS2 >= threshold:
        print('found match DC')
        S2 = 0
    else:
        print('not found match DC')
        S2 = 1

    if max_valS3 >= threshold:
        print('found match D00')
        S3 = 0

    else:
        print('not found match D00')
        S3 = 1

    if max_valS4 >= threshold:
        print('found match D01')
        S4 = 0

    else:
        print('not found match D01')
        S4 = 1

    if max_valS5 >= threshold:
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

