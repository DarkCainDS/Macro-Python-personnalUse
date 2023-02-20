import cv2
import numpy as np
import pyautogui
Diego1000 = [
  '0_0.png',  '0_1.png',  '0_2.png',  '0_3.png',  '0_4.png',
  '0_5.png',  '0_6.png',  '0_7.png',  '0_8.png',  '0_9.png',
  '0_10.png', '0_11.png', '0_12.png', '0_13.png', '0_14.png',
  '0_15.png', '0_16.png', '0_17.png', '0_18.png', '0_19.png',
  '0_20.png', '0_21.png', '0_22.png', '0_23.png', '0_24.png',
  '0_25.png', '0_26.png', '0_27.png', '0_28.png', '0_29.png',
  '0_30.png', '0_31.png', '0_32.png', '0_33.png', '0_34.png',
  '0_35.png', '0_36.png', '0_37.png', '0_38.png', '0_39.png',
  '0_40.png', '0_41.png', '0_42.png', '0_43.png', '0_44.png',
  '0_45.png', '0_46.png', '0_47.png', '0_48.png', '0_49.png',
  '0_50.png', '0_51.png', '0_52.png', '0_53.png', '0_54.png',
  '0_55.png', '0_56.png', '0_57.png', '0_58.png', '0_59.png',
  '0_60.png', '0_61.png', '0_62.png', '0_63.png', '0_64.png',
  '0_65.png', '0_66.png', '0_67.png', '0_68.png', '0_69.png',
  '0_70.png', '0_71.png', '0_72.png', '0_73.png', '0_74.png',
  '0_75.png', '0_76.png', '0_77.png', '0_78.png', '0_79.png',
  '0_80.png', '0_81.png', '0_82.png', '0_83.png', '0_84.png',
  '0_85.png', '0_86.png', '0_87.png', '0_88.png', '0_89.png',
  '0_90.png', '0_91.png', '0_92.png', '0_93.png', '0_94.png',
  '0_95.png', '0_96.png', '0_97.png', '0_98.png', '0_99.png'
]

def encontrar_plantilla(imagen, plantilla):
    img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    plantilla_img = cv2.imread(plantilla, 0)
    res = cv2.matchTemplate(img_gris, plantilla_img, cv2.TM_CCOEFF_NORMED)
    umbral = 0.8
    loc = np.where(res >= umbral)
    return loc

imagen =  pyautogui.screenshot() #cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)
imagen = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGB2BGR)


cv2.imwrite("in_memory_to_disk.png", imagen)

imagen = cv2.imread('in_memory_to_disk.png')


for plantilla in Diego1000:
    loc = encontrar_plantilla(imagen, plantilla)
    w, h = cv2.imread(plantilla, 0).shape[::-1]
    for pt in zip(*loc[::-1]):
        cv2.rectangle(imagen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('Imagen', imagen)

