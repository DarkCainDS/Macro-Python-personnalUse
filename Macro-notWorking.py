
"""
import cv2
import numpy as np

diego1001 = cv2.imread('diego1001.png', cv2.IMREAD_UNCHANGED)
findOpponent = cv2.imread('findOpponent.png', cv2.IMREAD_UNCHANGED)
desktop = cv2.imread('desktop-5-Screen.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(desktop, findOpponent, cv2.TM_CCOEFF_NORMED)

w = findOpponent.shape[1]
h = findOpponent.shape[0]



min_val, max_val, min_loc, max_loc =  cv2.minMaxLoc(result)
squareBox = cv2.rectangle(desktop, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255),2)


print(max_loc)
print(max_val)

threshold = .60
yloc, xloc = np.where(result >= threshold)
len(xloc)
for(x,y) in zip(xloc,yloc):
    cv2.rectangle(desktop, (x,y), (x + w, y+ h),(0,255,255),2)

result = cv2.matchTemplate(desktop, findOpponent, cv2.TM_CCOEFF_NORMED)


cv2.imshow('Desktop', desktop)
cv2.waitKey()
cv2.destroyAllWindows()


"""

import cv2 
import numpy as np

minirana = cv2.imread('minirana.png', cv2.IMREAD_UNCHANGED)
darkcloud = cv2.imread('darkcloud.png', cv2.IMREAD_UNCHANGED)
diego1000 = cv2.imread('diego1000.png', cv2.IMREAD_UNCHANGED)
diego1001 = cv2.imread('diego1001.png', cv2.IMREAD_UNCHANGED)
diego1002 = cv2.imread('diego1002.png', cv2.IMREAD_UNCHANGED)
findOpponent = cv2.imread('findOpponent.png', cv2.IMREAD_UNCHANGED)
desktop = cv2.imread('desktop3.png', cv2.IMREAD_UNCHANGED)


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

print(min_val)
print(max_val)
print(min_val2)
print(max_val2)
print(min_val3)
print(max_val3)
print(min_val4)
print(max_val4)
print(min_val5)
print(max_val5)

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



cv2.imshow('Desktop', desktop)



