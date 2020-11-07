import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread('img/profile.jpg',cv2.IMREAD_COLOR)
cv2.rectangle(img, (55,55), (200,150), (0,255,0), 5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

