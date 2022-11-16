import pyautogui 
import time

minirana = pyautogui.locateOnScreen('minirana.png', confidence=0.8)
darkcloud = pyautogui.locateOnScreen('darkcloud.png',confidence=0.8, grayscale = True )
diego1000 = pyautogui.locateOnScreen('diego1000.png',confidence=0.8, grayscale = True )
diego1001 = pyautogui.locateOnScreen('diego1001.png',confidence=0.8, grayscale = True )
diego1002 = pyautogui.locateOnScreen('diego1002.png',confidence=0.8, grayscale = True )

for i in range(300):

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
    time.sleep(2)

    if minirana == None:
        pyautogui.click(x=1895, y=261)
        xyz = pyautogui.locateOnScreen('dragonary.png',  confidence=0.8, grayscale = True )
        pyautogui.click(xyz)
    elif darkcloud == None:
        pyautogui.click(x=1895, y=925)
        xyz = pyautogui.locateOnScreen('dragonary.png',  confidence=0.8, grayscale = True )
        pyautogui.click(xyz)
    elif diego1000 == None:
        pyautogui.click(x=875, y=960)
        xyz = pyautogui.locateOnScreen('dragonary.png',  confidence=0.8, grayscale = True )
        pyautogui.click(xyz)
    elif diego1001 == None:
        pyautogui.click(x=880, y=432)
        xyz = pyautogui.locateOnScreen('dragonary.png',  confidence=0.8, grayscale = True )
        pyautogui.click(xyz)
    elif diego1002 == None:
        pyautogui.click(x=1895, y=591)
        xyz = pyautogui.locateOnScreen('dragonary.png',  confidence=0.8, grayscale = True )
        pyautogui.click(xyz)
    

    


        
