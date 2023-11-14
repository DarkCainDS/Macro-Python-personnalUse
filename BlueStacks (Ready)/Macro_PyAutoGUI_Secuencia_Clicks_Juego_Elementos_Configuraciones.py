import pyautogui
import keyboard
import time

def click_sequence_element_first_fire():
    #Mission
    pyautogui.click(x=543, y=473)
    pyautogui.click(x=1172, y=424)
    pyautogui.click(x=1733, y=429)
    pyautogui.click(x=542, y=1000)
    pyautogui.click(x=1164, y=874)
    time.sleep(1)
    #Embers
    pyautogui.click(x=377, y=310)
    pyautogui.click(x=1068, y=285)
    pyautogui.click(x=1638, y=281)
    pyautogui.click(x=376, y=837)
    pyautogui.click(x=1042, y=742)
    time.sleep(1)
    #Difficult Level
    pyautogui.click(x=492, y=118)
    pyautogui.click(x=1132, y=110)
    pyautogui.click(x=1701, y=108)
    pyautogui.click(x=492, y=648)
    pyautogui.click(x=1128, y=567)
    time.sleep(1)
    #Element
    pyautogui.click(x=167, y=134)
    pyautogui.click(x=906, y=132)
    pyautogui.click(x=1467, y=126)
    pyautogui.click(x=160, y=662)
    pyautogui.click(x=900, y=587)
    time.sleep(1)
    #Play
    pyautogui.click(x=497, y=423)
    pyautogui.click(x=1129, y=383)
    pyautogui.click(x=1702, y=385)
    pyautogui.click(x=502, y=959)
    pyautogui.click(x=1136, y=843)

def click_sequence_start():
    pyautogui.click(x=388, y=335)#Start
    pyautogui.click(x=1058, y=300)
    pyautogui.click(x=1617, y=302)
    pyautogui.click(x=378, y=866)
    pyautogui.click(x=1057, y=760)
    time.sleep(1)
    pyautogui.click(x=328, y=62)# from manual to auto
    pyautogui.click(x=1022, y=57)
    pyautogui.click(x=1590, y=58)
    pyautogui.click(x=332, y=585)
    pyautogui.click(x=1018, y=532)
    time.sleep(1)
    pyautogui.click(x=428, y=60) # 1xvel to 2xvel
    pyautogui.click(x=1089, y=60)
    pyautogui.click(x=1656, y=60)
    pyautogui.click(x=429, y=584)
    pyautogui.click(x=1090, y=519)
def click_sequence_next():
    pyautogui.click(x=379, y=455) # Next
    pyautogui.click(x=1051, y=413)
    pyautogui.click(x=1626, y=409)
    pyautogui.click(x=384, y=981)
    pyautogui.click(x=1049, y=872)
def click_sequence_element_whitout_ember(f1,f1_5,f2,f2_5,f3,f3_5,f4,f4_5,f5,f5_5):
    #Mission
    pyautogui.click(x=543, y=473)
    pyautogui.click(x=1172, y=424)
    pyautogui.click(x=1733, y=429)
    pyautogui.click(x=542, y=1000)
    pyautogui.click(x=1164, y=874)
    time.sleep(1)
    #Difficult Level
    pyautogui.click(x=492, y=118)
    pyautogui.click(x=1132, y=110)
    pyautogui.click(x=1701, y=108)
    pyautogui.click(x=492, y=648)
    pyautogui.click(x=1128, y=567)
    time.sleep(1)
    #Element
    pyautogui.click(x=f1, y=f1_5)
    pyautogui.click(x=f2, y=f2_5)
    pyautogui.click(x=f3, y=f3_5)
    pyautogui.click(x=f4, y=f4_5)
    pyautogui.click(x=f5, y=f5_5)
    time.sleep(1)
    #Play
    pyautogui.click(x=497, y=423)
    pyautogui.click(x=1129, y=383)
    pyautogui.click(x=1702, y=385)
    pyautogui.click(x=502, y=959)
    pyautogui.click(x=1136, y=843)

def main():
    print("Presiona la tecla '1' para realizar la secuencia de clicks. Presiona 'ESC' para salir.")

    while True:
        if keyboard.is_pressed('esc'):
            break4
        if keyboard.is_pressed('1'):
            click_sequence_element_whitout_ember(167,134,906,132,1467,126,160,662,900,587)
            print("Fire:1")
            
        if keyboard.is_pressed('2'):
            click_sequence_element_whitout_ember(163,187,893,171,1470,169,167,713,900,628)
            print("Earth:2")

        if keyboard.is_pressed('3'):
            click_sequence_element_whitout_ember(161,227,905,216,1471,214,170,760,900,674)
            print("Air:3")

        if keyboard.is_pressed('4'):
            click_sequence_element_whitout_ember(164,283,899,258,1473,253,167,809,900,715)
            print("Electric:4")
            
        if keyboard.is_pressed('5'):
            click_sequence_element_whitout_ember(163,328,900,300,1468,302,163,857,900,760)
            print("Plant:5")
        if keyboard.is_pressed('6'):
            click_sequence_element_whitout_ember(158,374,906,337,1470,335,158,905,900,798)
            print("Water:6")

        if keyboard.is_pressed('7'):
            click_sequence_element_whitout_ember(171,427,902,383,1471,383,167,958,900,844)
            print("Ice:7")

        if keyboard.is_pressed('8'):
            click_sequence_next()
            
        if keyboard.is_pressed('9'):
            click_sequence_start()
            
        if keyboard.is_pressed('0'):
            click_sequence_element_first_fire()
            


if __name__ == "__main__":
    main()
# 1001 Fire:167,134 Earth:163,187   Air:161,227 Electric:164,283    Plant:163,328   Water:158,374   Ice:171,427
# 1002 Fire:906,132 Earth:893,171   Air:905,216 Electric:899,258    Plant:900,300   Water:906,337   Ice:902,383
# Minirana Fire:1467,126 Earth:1470,169   Air:1471,214 Electric:1473,253    Plant:1468,302   Water:1470,335   Ice:1471,383
# 1000 Fire:160,662 Earth:167,713   Air:170,760 Electric:167,809    Plant:163,857   Water:158,905   Ice:167,958
# Darkcloud Fire:900,587 Earth:900,628   Air:900,674 Electric:900,715    Plant:900,760   Water:900,798   Ice:900,844
