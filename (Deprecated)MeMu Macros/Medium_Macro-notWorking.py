import pyautogui 
import time
import cv2 
import numpy as np
"""
desktopTest = pyautogui.screenshot()
desktopTest = cv2.cvtColor(np.array(desktopTest), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", desktopTest)
"""





for i in range(300):
    
    minirana = cv2.imread('minirana.png', cv2.IMREAD_UNCHANGED)
    darkcloud = cv2.imread('darkcloud.png', cv2.IMREAD_UNCHANGED)
    diego1000 = cv2.imread('diego1000.png', cv2.IMREAD_UNCHANGED)
    diego1001 = cv2.imread('diego1001.png', cv2.IMREAD_UNCHANGED)
    diego1002 = cv2.imread('diego1002.png', cv2.IMREAD_UNCHANGED)
    findOpponent = cv2.imread('findOpponent.png', cv2.IMREAD_UNCHANGED)

    desktop =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
    desktop = cv2.cvtColor(np.array(desktop), cv2.COLOR_RGB2BGR)
    cv2.imwrite("in_memory_to_disk.png", desktop)

    result = cv2.matchTemplate(desktop, minirana, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(desktop, darkcloud, cv2.TM_CCOEFF_NORMED)
    result3 = cv2.matchTemplate(desktop, diego1000, cv2.TM_CCOEFF_NORMED)
    result4 = cv2.matchTemplate(desktop, diego1001, cv2.TM_CCOEFF_NORMED)
    result5 = cv2.matchTemplate(desktop, diego1002, cv2.TM_CCOEFF_NORMED)


    min_val, max_val, min_loc, max_loc =  cv2.minMaxLoc(result)
    min_val2, max_val2, min_loc2, max_loc2 =  cv2.minMaxLoc(result2)
    min_val3, max_val3, min_loc3, max_loc3 =  cv2.minMaxLoc(result3)
    min_val4, max_val4, min_loc4, max_loc4 =  cv2.minMaxLoc(result4)
    min_val5, max_val5, min_loc5, max_loc5 =  cv2.minMaxLoc(result5)
    """
    print(max_val)
    print(max_val2)
    print(max_val3)
    print(max_val4)
    print(max_val5)
    """
    w = minirana.shape[1]
    h = minirana.shape[0]

    w2 = darkcloud.shape[1]
    h2 = darkcloud.shape[0]

    w3 = diego1000.shape[1]
    h3 = diego1000.shape[0]

    w4 = diego1001.shape[1]
    h4 = diego1001.shape[0]

    w5 = diego1002.shape[1]
    h5 = diego1002.shape[0]

    squareBox = cv2.rectangle(desktop, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255),2)
    squareBox2 = cv2.rectangle(desktop, max_loc2, (max_loc2[0] + w2, max_loc2[1] + h2), (0,255,255),2)
    squareBox3 = cv2.rectangle(desktop, max_loc3, (max_loc3[0] + w3, max_loc3[1] + h3), (0,255,255),2)
    squareBox4 = cv2.rectangle(desktop, max_loc4, (max_loc4[0] + w4, max_loc4[1] + h4), (0,255,255),2)
    squareBox5 = cv2.rectangle(desktop, max_loc5, (max_loc5[0] + w5, max_loc5[1] + h5), (0,255,255),2)


    #Find Opponent
    pyautogui.click(x=426, y=934)
    pyautogui.click(x=426, y=411)
    pyautogui.click(x=1570, y=272)
    pyautogui.click(x=1570, y=607)
    pyautogui.click(x=1570, y=939)
    time.sleep(3)
    #Fight!
    pyautogui.click(x=608, y=341)
    pyautogui.click(x=608, y=866)
    pyautogui.click(x=1700, y=224)
    pyautogui.click(x=1700, y=561)
    pyautogui.click(x=1700, y=893)
    time.sleep(4.5)
    #Collect
    pyautogui.click(x=426, y=448)
    pyautogui.click(x=426, y=975)
    pyautogui.click(x=1570, y=292)
    pyautogui.click(x=1570, y=627)
    pyautogui.click(x=1570, y=962)
    time.sleep(1)
    
    print('NEw Line')
    print(max_val)
    print(max_val2)
    print(max_val3)
    print(max_val4)
    print(max_val5)

        
