import cv2
import numpy as np
from scene_text import AllWordsRecognizer

img = cv2.imread('images/test.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # threshold image
ret, thresh = cv2.threshold(imgray, 150, 255, 0)
cv2.imwrite('thresh.jpg', thresh)

# edge contours
contours, hierarchy = cv2.findContours(thresh, 1, 2)

pipeline = AllWordsRecognizer()

# read an image
img = cv2.imread('thresh.jpg')

# detect and recognize all words in the image
words, boxes = pipeline.get_all_words(img)

count = 0

for box in boxes:
  class_name = type(box).__name__
  print(class_name)
  count += 1