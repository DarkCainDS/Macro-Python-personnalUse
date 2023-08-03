import cv2 as cv
import numpy as np
import pyautogui
import time

minirana = cv.imread('minirana_1.png', cv.IMREAD_UNCHANGED)
darkcloud = cv.imread('darkcloud_1.png', cv.IMREAD_UNCHANGED)
diego1000 = cv.imread('diego1000_1.png', cv.IMREAD_UNCHANGED)
diego1001 = cv.imread('diego1001_1.png', cv.IMREAD_UNCHANGED)
diego1002 = cv.imread('diego1002_1.png', cv.IMREAD_UNCHANGED)

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
    
      

    if S1 == 1 or S2 == 1 or S3 == 1 or S4 == 1 or S5 == 1:
        if S1 == 1:
            pyautogui.click(x=1900, y=412)
            time.sleep(1)
            pyautogui.click(x=1500, y=122)
            time.sleep(1)
            desktop =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
            desktop = cv.cvtColor(np.array(desktop), cv.COLOR_RGB2BGR)
            cv.imwrite("in_memory_to_disk.png", desktop)
        elif S2 == 1:
            pyautogui.click(x=1335, y=870)
            time.sleep(1)
            pyautogui.click(x=932, y=576)
            time.sleep(1)
            desktop =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
            desktop = cv.cvtColor(np.array(desktop), cv.COLOR_RGB2BGR)
            cv.imwrite("in_memory_to_disk.png", desktop)
        elif S3 == 1:
            pyautogui.click(x=765, y=989)
            time.sleep(1)
            pyautogui.click(x=200, y=650)
            time.sleep(1)
            desktop =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
            desktop = cv.cvtColor(np.array(desktop), cv.COLOR_RGB2BGR)
            cv.imwrite("in_memory_to_disk.png", desktop)
        elif S4 == 1:
            pyautogui.click(x=765, y=465)
            time.sleep(1)
            pyautogui.click(x=200, y=125)
            time.sleep(1)
            desktop =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
            desktop = cv.cvtColor(np.array(desktop), cv.COLOR_RGB2BGR)
            cv.imwrite("in_memory_to_disk.png", desktop)
        elif S5 == 1:
            pyautogui.click(x=1336, y=413)
            time.sleep(1)
            pyautogui.click(x=930, y=120)
            time.sleep(1)
            desktop =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
            desktop = cv.cvtColor(np.array(desktop), cv.COLOR_RGB2BGR)
            cv.imwrite("in_memory_to_disk.png", desktop)
            
        
    else :
        
        #Find Opponent
        counter = 0
        pyautogui.click(x=380, y=427)
        pyautogui.click(x=365, y=943)
        pyautogui.click(x=1052, y=380)
        pyautogui.click(x=1621, y=380)
        pyautogui.click(x=1044, y=840)
        time.sleep(4.5)
        #Fight!
        pyautogui.click(x=530, y=350)
        pyautogui.click(x=530, y=870)
        pyautogui.click(x=1150, y=320)
        pyautogui.click(x=1740, y=315)
        pyautogui.click(x=1175, y=770)
        time.sleep(5.5)
        #Collect
        pyautogui.click(x=390, y=460)
        pyautogui.click(x=390, y=975)
        pyautogui.click(x=1040, y=410)
        pyautogui.click(x=1610, y=410)
        pyautogui.click(x=1050, y=870)
        time.sleep(1)
        
for i in range(350):

    minirana = cv.imread('minirana_1.png', cv.IMREAD_UNCHANGED)
    darkcloud = cv.imread('darkcloud_1.png', cv.IMREAD_UNCHANGED)
    diego1000 = cv.imread('diego1000_1.png', cv.IMREAD_UNCHANGED)
    diego1001 = cv.imread('diego1001_1.png', cv.IMREAD_UNCHANGED)
    diego1002 = cv.imread('diego1002_1.png', cv.IMREAD_UNCHANGED)

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
    print(i)
    clicker(S1,S2,S3,S4,S5)
    
    desktop =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
    desktop = cv.cvtColor(np.array(desktop), cv.COLOR_RGB2BGR)
    cv.imwrite("in_memory_to_disk.png", desktop)
